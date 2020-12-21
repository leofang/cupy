import numpy as np

#cimport cython
#
#cimport libc.stdlib
#cimport libc.math
#
#
#ctypedef double complex double_complex
#
#cdef extern from "numpy/npy_math.h":
#    double nan "NPY_NAN"
#
#DEF MAX_DIMS = 64


#------------------------------------------------------------------------------
# Piecewise power basis polynomials
#------------------------------------------------------------------------------

def evaluate(c,  # double or complex
             x,  # double
             xp,  # double
             dx,  # int 
             extrapolate,  # bool
             out):  # double or complex
    """
    Evaluate a piecewise polynomial.

    Parameters
    ----------
    c : ndarray, shape (k, m, n)
        Coefficients local polynomials of order `k-1` in `m` intervals.
        There are `n` polynomials in each interval.
        Coefficient of highest order-term comes first.
    x : ndarray, shape (m+1,)
        Breakpoints of polynomials.
    xp : ndarray, shape (r,)
        Points to evaluate the piecewise polynomial at.
    dx : int
        Order of derivative to evaluate.  The derivative is evaluated
        piecewise and may have discontinuities.
    extrapolate : bint
        Whether to extrapolate to out-of-bounds points based on first
        and last intervals, or to return NaNs.
    out : ndarray, shape (r, n)
        Value of each polynomial at each of the input points.
        This argument is modified in-place.

    """
    cdef int ip, jp
    cdef int interval
    cdef double xval

    # check derivative order
    if dx < 0:
        raise ValueError("Order of derivative cannot be negative")

    # shape checks
    if out.shape[0] != xp.shape[0]:
        raise ValueError("out and xp have incompatible shapes")
    if out.shape[1] != c.shape[2]:
        raise ValueError("out and c have incompatible shapes")
    if c.shape[1] != x.shape[0] - 1:
        raise ValueError("x and c have incompatible shapes")

    interval = 0
    cdef bint ascending = x[x.shape[0] - 1] >= x[0]

    # Evaluate.
    for ip in range(len(xp)):
        xval = xp[ip]

        # Find correct interval
        if ascending:
            i = find_interval_ascending(&x[0], x.shape[0], xval, interval,
                                        extrapolate)
        else:
            i = find_interval_descending(&x[0], x.shape[0], xval, interval,
                                         extrapolate)
        if i < 0:
            # xval was nan etc
            for jp in range(c.shape[2]):
                out[ip, jp] = nan
            continue
        else:
            interval = i

        # Evaluate the local polynomial(s)
        for jp in range(c.shape[2]):
            out[ip, jp] = evaluate_poly1(xval - x[interval], c, interval,
                                         jp, dx)


# TODO(leofang): Add evaluate_nd


def fix_continuity(c,  # double or complex
                   x,  # double
                   order):  # int
    """
    Make a piecewise polynomial continuously differentiable to given order.

    Parameters
    ----------
    c : ndarray, shape (k, m, n)
        Coefficients local polynomials of order `k-1` in `m` intervals.
        There are `n` polynomials in each interval.
        Coefficient of highest order-term comes first.

        Coefficients c[-order-1:] are modified in-place.
    x : ndarray, shape (m+1,)
        Breakpoints of polynomials
    order : int
        Order up to which enforce piecewise differentiability.

    """

    cdef int ip, jp, kp, dx
    cdef int interval
    cdef double_or_complex res
    cdef double xval

    # check derivative order
    if order < 0:
        raise ValueError("Order of derivative cannot be negative")

    # shape checks
    if c.shape[1] != x.shape[0] - 1:
        raise ValueError("x and c have incompatible shapes")
    if order >= c.shape[0] - 1:
        raise ValueError("order too large")
    if order < 0:
        raise ValueError("order negative")

    # evaluate
    for ip in range(1, len(x)-1):
        xval = x[ip]
        interval = ip - 1

        for jp in range(c.shape[2]):
            # ensure continuity for derivatives, starting at the
            # highest one (the lower derivatives depend on the higher
            # ones, but not vice versa)
            for dx in range(order, -1, -1):
                # evaluate dx-th derivative of the polynomial in previous interval
                res = evaluate_poly1(xval - x[interval], c, interval, jp, dx)

                # set dx-th coefficient of polynomial in current
                # interval so that the dx-th derivative is continuous
                for kp in range(dx):
                    res /= kp + 1

                c[c.shape[0] - dx - 1, ip, jp] = res


# TODO(leofang): Add integrate


# TODO(leofang): Add real_roots


cdef int find_interval_ascending(const double *x,
                                 size_t nx,
                                 double xval,
                                 int prev_interval=0,
                                 bint extrapolate=1) nogil:
    """
    Find an interval such that x[interval] <= xval < x[interval+1]. Assuming
    that x is sorted in the ascending order.
    If xval < x[0], then interval = 0, if xval > x[-1] then interval = n - 2.

    Parameters
    ----------
    x : array of double, shape (m,)
        Piecewise polynomial breakpoints sorted in ascending order.
    xval : double
        Point to find.
    prev_interval : int, optional
        Interval where a previous point was found.
    extrapolate : bint, optional
        Whether to return the last of the first interval if the
        point is out-of-bounds.

    Returns
    -------
    interval : int
        Suitable interval or -1 if nan.

    """
    cdef int interval, high, low, mid
    cdef double a, b

    a = x[0]
    b = x[nx-1]

    interval = prev_interval
    if interval < 0 or interval >= nx:
        interval = 0

    if not (a <= xval <= b):
        # Out-of-bounds (or nan)
        if xval < a and extrapolate:
            # below
            interval = 0
        elif xval > b and extrapolate:
            # above
            interval = nx - 2
        else:
            # nan or no extrapolation
            interval = -1
    elif xval == b:
        # Make the interval closed from the right
        interval = nx - 2
    else:
        # Find the interval the coordinate is in
        # (binary search with locality)
        if xval >= x[interval]:
            low = interval
            high = nx - 2
        else:
            low = 0
            high = interval

        if xval < x[low+1]:
            high = low

        while low < high:
            mid = (high + low)//2
            if xval < x[mid]:
                # mid < high
                high = mid
            elif xval >= x[mid + 1]:
                low = mid + 1
            else:
                # x[mid] <= xval < x[mid+1]
                low = mid
                break

        interval = low

    return interval


cdef int find_interval_descending(const double *x,
                                 size_t nx,
                                 double xval,
                                 int prev_interval=0,
                                 bint extrapolate=1) nogil:
    """
    Find an interval such that x[interval + 1] < xval <= x[interval], assuming
    that x are sorted in the descending order.
    If xval > x[0], then interval = 0, if xval < x[-1] then interval = n - 2.

    Parameters
    ----------
    x : array of double, shape (m,)
        Piecewise polynomial breakpoints sorted in descending order.
    xval : double
        Point to find.
    prev_interval : int, optional
        Interval where a previous point was found.
    extrapolate : bint, optional
        Whether to return the last of the first interval if the
        point is out-of-bounds.

    Returns
    -------
    interval : int
        Suitable interval or -1 if nan.

    """
    cdef int interval, high, low, mid
    cdef double a, b

    # Note that now a > b.
    a = x[0]
    b = x[nx-1]

    interval = prev_interval
    if interval < 0 or interval >= nx:
        interval = 0

    if not (b <= xval <= a):
        # Out-of-bounds or NaN.
        if xval > a and extrapolate:
            # Above a.
            interval = 0
        elif xval < b and extrapolate:
            # Below b.
            interval = nx - 2
        else:
            # No extrapolation.
            interval = -1
    elif xval == b:
        # Make the interval closed from the left.
        interval = nx - 2
    else:
        # Apply the binary search in a general case. Note that low and high
        # are used in terms of interval number, not in terms of abscissas.
        # The conversion from find_interval_ascending is simply to change
        # < to > and >= to <= in comparison with xval.
        if xval <= x[interval]:
            low = interval
            high = nx - 2
        else:
            low = 0
            high = interval

        if xval > x[low + 1]:
            high = low

        while low < high:
            mid = (high + low) // 2
            if xval > x[mid]:
                # mid < high
                high = mid
            elif xval <= x[mid + 1]:
                low = mid + 1
            else:
                # x[mid] >= xval > x[mid+1]
                low = mid
                break

        interval = low

    return interval


cdef double_or_complex evaluate_poly1(double s, double_or_complex[:,:,::1] c, int ci, int cj, int dx) nogil:
    """
    Evaluate polynomial, derivative, or antiderivative in a single interval.

    Antiderivatives are evaluated assuming zero integration constants.

    Parameters
    ----------
    s : double
        Polynomial x-value
    c : double[:,:,:]
        Polynomial coefficients. c[:,ci,cj] will be used
    ci, cj : int
        Which of the coefs to use
    dx : int
        Order of derivative (> 0) or antiderivative (< 0) to evaluate.

    """
    cdef int kp, k
    cdef double_or_complex res, z
    cdef double prefactor

    res = 0.0
    z = 1.0

    if dx < 0:
        for k in range(-dx):
            z *= s

    for kp in range(c.shape[0]):
        # prefactor of term after differentiation
        if dx == 0:
            prefactor = 1.0
        elif dx > 0:
            # derivative
            if kp < dx:
                continue
            else:
                prefactor = 1.0
                for k in range(kp, kp - dx, -1):
                    prefactor *= k
        else:
            # antiderivative
            prefactor = 1.0
            for k in range(kp, kp - dx):
                prefactor /= k + 1

        res = res + c[c.shape[0] - kp - 1, ci, cj] * z * prefactor

        # compute x**max(k-dx,0)
        if kp < c.shape[0] - 1 and kp >= dx:
            z *= s

    return res


# TODO(leofang): Add croots_poly1


# TODO(leofang): Add evaluate_bpoly1


# TODO(leofang): Add evaluate_bpoly1_deriv


# TODO(leofang): Add evaluate_bernstein

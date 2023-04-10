
import cupy
from cupyx.scipy.signal._signaltools import lfilter


def _find_initial_cond(all_valid, cum_poly, n):
    indices = cupy.where(all_valid)[0] + 1
    zi = cupy.nan
    if indices.size > 0:
        zi = cupy.where(
            indices[0] >= n, cupy.nan, cum_poly[indices[0] - 1])
    return zi


def symiirorder1(input, c0, z1, precision=-1.0):
    """
    Implement a smoothing IIR filter with mirror-symmetric boundary conditions
    using a cascade of first-order sections.  The second section uses a
    reversed sequence.  This implements a system with the following
    transfer function and mirror-symmetric boundary conditions::

                           c0
           H(z) = ---------------------
                   (1-z1/z) (1 - z1 z)

    The resulting signal will have mirror symmetric boundary conditions
    as well.

    Parameters
    ----------
    input : ndarray
        The input signal.
    c0, z1 : scalar
        Parameters in the transfer function.
    precision :
        Specifies the precision for calculating initial conditions
        of the recursive filter based on mirror-symmetric input.

    Returns
    -------
    output : ndarray
        The filtered signal.
    """

    if cupy.abs(z1) >= 1:
        raise ValueError('|z1| must be less than 1.0')

    if precision <= 0.0 or precision > 1.0:
        precision = cupy.finfo(input.dtype).resolution

    precision *= precision
    pos = cupy.arange(1, input.size + 1, dtype=input.dtype)
    pow_z1 = z1 ** pos

    diff = pow_z1 * cupy.conjugate(pow_z1)
    cum_poly = cupy.cumsum(pow_z1 * input) + input[0]
    all_valid = diff <= precision

    zi = _find_initial_cond(all_valid, cum_poly, input.size)

    if cupy.isnan(zi):
        raise ValueError(
            'Sum to find symmetric boundary conditions did not converge.')

    # Apply first the system 1 / (1 - z1 * z^-1)
    y1, _ = lfilter(
        cupy.ones(1, dtype=input.dtype), cupy.r_[1, -z1], input[1:], zi=zi)
    y1 = cupy.r_[zi, y1]

    # Compute backward symmetric condition and apply the system
    # c0 / (1 - z1 * z)
    zi = -c0 / (z1 - 1.0) * y1[-1]
    out, _ = lfilter(c0, cupy.r_[1, -z1], y1[:-1][::-1], zi=zi)
    return cupy.r_[out[::-1], zi]


def _compute_symiirorder2_fwd_hc(k, cs, r, omega):
    if k < 0:
        return 0.0
    if omega == 0.0:
        return cs * cupy.pow(r, k) * (k+1)
    elif omega == cupy.pi:
        return cs * cupy.pow(r, k) * (k + 1) * (1 - 2 * (k % 2))
    return cs * cupy.pow(r, k) * cupy.sin(omega * (k+1)) / cupy.sin(omega)


def symiirorder2(input, r, omega, precision=-1.0):
    """
    Implement a smoothing IIR filter with mirror-symmetric boundary conditions
    using a cascade of second-order sections.  The second section uses a
    reversed sequence.  This implements the following transfer function::

                                  cs^2
         H(z) = ---------------------------------------
                (1 - a2/z - a3/z^2) (1 - a2 z - a3 z^2 )

    where::

          a2 = 2 * r * cos(omega)
          a3 = - r ** 2
          cs = 1 - 2 * r * cos(omega) + r ** 2

    Parameters
    ----------
    input : ndarray
        The input signal.
    r, omega : float
        Parameters in the transfer function.
    precision : float
        Specifies the precision for calculating initial conditions
        of the recursive filter based on mirror-symmetric input.

    Returns
    -------
    output : ndarray
        The filtered signal.
    """
    if r >= 1.0:
        raise ValueError('r must be less than 1.0')

    if precision <= 0.0 or precision > 1.0:
        precision = cupy.finfo(input.dtype).resolution

    rsq = r * r
    a2 = 2 * r * cupy.cos(omega)
    a3 = -rsq
    cs = 1 - 2 * r * cupy.cos(omega) + rsq

    precision *= precision
    pos = cupy.arange(0, input.size + 2, dtype=input.dtype)
    diff = _compute_symiirorder2_fwd_hc(pos, cs, r, omega)
    err = diff * diff
    cum_poly_y0 = cupy.cumsum(diff[1:-1] * input) + diff[0] * input[0]

    overflow = False
    y0 = cum_poly_y0[0]
    if precision != 1.0:
        all_valid = err <= precision
        valid_before = all_valid[1:-1]
        valid_after = all_valid[:-2]
        valid = cupy.logical_xor(valid_before, valid_after)
        valid_starting = cupy.where(valid, cum_poly_y0, cupy.nan)
        y0 = cupy.nanmax(valid_starting, keepdims=True)
        zi_pos = pos[1:-1][valid]
        overflow = cupy.where(zi_pos >= input.size, True, False)

    if cupy.isnan(y0) or overflow:
        raise ValueError(
            'Sum to find symmetric boundary conditions did not converge.')

    cum_poly_y1 = (cupy.cumsum(diff[2:] * input) +
                   diff[0] * input[1] + diff[1] * input[0])
    y1 = cum_poly_y1[0]
    if precision != 1.0:
        all_valid = err <= precision
        valid_before = all_valid[2:]
        valid_after = all_valid[:-1]
        valid = cupy.logical_xor(valid_before, valid_after)
        valid_starting = cupy.where(valid, cum_poly_y1, cupy.nan)
        y1 = cupy.nanmax(valid_starting, keepdims=True)
        zi_pos = pos[1:-1][valid]
        overflow = cupy.where(zi_pos >= input.size, True, False)

    zi = cupy.r_[y0, y1]
    # Apply first the system cs / (1 - a2 * z^-1 - a3 * z^-2)
    y1, _ = lfilter(cs, cupy.r_[1, -a2, -a3], input[2:], zi=zi)

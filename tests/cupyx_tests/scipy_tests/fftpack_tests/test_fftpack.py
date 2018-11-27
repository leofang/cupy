import unittest

from cupy import testing
import cupyx.scipy.fftpack  # NOQA

if cupyx.scipy._scipy_available:
    import scipy.fftpack  # NOQA


@testing.parameterize(*testing.product({
    'n': [None, 0, 5, 10, 15],
    'shape': [(9,), (10,), (10, 9), (10, 10)],
    'axis': [-1, 0],
}))
@testing.gpu
@testing.with_requires('scipy')
class TestFft(unittest.TestCase):

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose(rtol=1e-4, atol=1e-7, accept_error=ValueError,
                                 contiguous_check=False, scipy_name='scp')
    def test_fft(self, xp, scp, dtype):
        x = testing.shaped_random(self.shape, xp, dtype)
        x_orig = x.copy()
        out = scp.fftpack.fft(x, n=self.n, axis=self.axis)
        testing.assert_array_equal(x, x_orig)
        return out

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose(rtol=1e-4, atol=1e-7, accept_error=ValueError,
                                 contiguous_check=False, scipy_name='scp')
    def test_fft_overwrite(self, xp, scp, dtype):
        x = testing.shaped_random(self.shape, xp, dtype)
        return scp.fftpack.fft(x, n=self.n, axis=self.axis,
                               overwrite_x=True)

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose(rtol=1e-4, atol=1e-7, accept_error=ValueError,
                                 contiguous_check=False, scipy_name='scp')
    def test_ifft(self, xp, scp, dtype):
        x = testing.shaped_random(self.shape, xp, dtype)
        x_orig = x.copy()
        out = scp.fftpack.ifft(x, n=self.n, axis=self.axis)
        testing.assert_array_equal(x, x_orig)
        return out

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose(rtol=1e-4, atol=1e-7, accept_error=ValueError,
                                 contiguous_check=False, scipy_name='scp')
    def test_ifft_overwrite(self, xp, scp, dtype):
        x = testing.shaped_random(self.shape, xp, dtype)
        return scp.fftpack.ifft(x, n=self.n, axis=self.axis,
                                overwrite_x=True)


@testing.parameterize(
    {'shape': (3, 4), 's': None, 'axes': None},
    {'shape': (3, 4), 's': (1, 5), 'axes': None},
    {'shape': (3, 4), 's': None, 'axes': (-2, -1)},
    {'shape': (3, 4), 's': None, 'axes': (-1, -2)},
    {'shape': (3, 4), 's': None, 'axes': (0,)},
    {'shape': (2, 3, 4), 's': None, 'axes': None},
    {'shape': (2, 3, 4), 's': (1, 4, 10), 'axes': None},
    {'shape': (2, 3, 4), 's': None, 'axes': (-3, -2, -1)},
    {'shape': (2, 3, 4), 's': None, 'axes': (-1, -2, -3)},
    {'shape': (2, 3, 4), 's': None, 'axes': (0, 1)},
    {'shape': (2, 3, 4, 5), 's': None, 'axes': None},
)
@testing.gpu
@testing.with_requires('scipy')
class TestFft2(unittest.TestCase):

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose(rtol=1e-4, atol=1e-7, accept_error=ValueError,
                                 contiguous_check=False, scipy_name='scp')
    def test_fft2(self, xp, scp, dtype):
        x = testing.shaped_random(self.shape, xp, dtype)
        x_orig = x.copy()
        out = scp.fftpack.fft2(x, shape=self.s, axes=self.axes)
        testing.assert_array_equal(x, x_orig)
        return out

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose(rtol=1e-4, atol=1e-7, accept_error=ValueError,
                                 contiguous_check=False, scipy_name='scp')
    def test_fft2_overwrite(self, xp, scp, dtype):
        x = testing.shaped_random(self.shape, xp, dtype)
        return scp.fftpack.fft2(x, shape=self.s, axes=self.axes,
                                overwrite_x=True)

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose(rtol=1e-4, atol=1e-7, accept_error=ValueError,
                                 contiguous_check=False, scipy_name='scp')
    def test_ifft2(self, xp, scp, dtype):
        x = testing.shaped_random(self.shape, xp, dtype)
        x_orig = x.copy()
        out = scp.fftpack.ifft2(x, shape=self.s, axes=self.axes)
        testing.assert_array_equal(x, x_orig)
        return out

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose(rtol=1e-4, atol=1e-7, accept_error=ValueError,
                                 contiguous_check=False, scipy_name='scp')
    def test_ifft2_overwrite(self, xp, scp, dtype):
        x = testing.shaped_random(self.shape, xp, dtype)
        return scp.fftpack.ifft2(x, shape=self.s, axes=self.axes,
                                 overwrite_x=True)


@testing.parameterize(
    {'shape': (3, 4), 's': None, 'axes': None},
    {'shape': (3, 4), 's': (1, 5), 'axes': None},
    {'shape': (3, 4), 's': None, 'axes': (-2, -1)},
    {'shape': (3, 4), 's': None, 'axes': (-1, -2)},
    {'shape': (3, 4), 's': None, 'axes': (0,)},
    {'shape': (2, 3, 4), 's': None, 'axes': None},
    {'shape': (2, 3, 4), 's': (1, 4, 10), 'axes': None},
    {'shape': (2, 3, 4), 's': None, 'axes': (-3, -2, -1)},
    {'shape': (2, 3, 4), 's': None, 'axes': (-1, -2, -3)},
    {'shape': (2, 3, 4), 's': None, 'axes': (0, 1)},
    {'shape': (2, 3, 4, 5), 's': None, 'axes': None},
)
@testing.gpu
@testing.with_requires('scipy')
class TestFftn(unittest.TestCase):

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose(rtol=1e-4, atol=1e-7, accept_error=ValueError,
                                 contiguous_check=False, scipy_name='scp')
    def test_fftn(self, xp, scp, dtype):
        x = testing.shaped_random(self.shape, xp, dtype)
        x_orig = x.copy()
        out = scp.fftpack.fftn(x, shape=self.s, axes=self.axes)
        testing.assert_array_equal(x, x_orig)
        return out

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose(rtol=1e-4, atol=1e-7, accept_error=ValueError,
                                 contiguous_check=False, scipy_name='scp')
    def test_fftn_overwrite(self, xp, scp, dtype):
        x = testing.shaped_random(self.shape, xp, dtype)
        return scp.fftpack.fftn(x, shape=self.s, axes=self.axes,
                                overwrite_x=True)

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose(rtol=1e-4, atol=1e-7, accept_error=ValueError,
                                 contiguous_check=False, scipy_name='scp')
    def test_ifftn(self, xp, scp, dtype):
        x = testing.shaped_random(self.shape, xp, dtype)
        x_orig = x.copy()
        out = scp.fftpack.ifftn(x, shape=self.s, axes=self.axes)
        testing.assert_array_equal(x, x_orig)
        return out

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose(rtol=1e-4, atol=1e-7, accept_error=ValueError,
                                 contiguous_check=False, scipy_name='scp')
    def test_ifftn_overwrite(self, xp, scp, dtype):
        x = testing.shaped_random(self.shape, xp, dtype)
        return scp.fftpack.ifftn(x, shape=self.s, axes=self.axes,
                                 overwrite_x=True)


@testing.parameterize(*testing.product({
    'n': [None, 5, 10, 15],
    'shape': [(9,), (10,), (10, 9), (10, 10)],
    'axis': [-1, 0],
}))
@testing.gpu
@testing.with_requires('scipy')
class TestRfft(unittest.TestCase):

    @testing.for_all_dtypes(no_complex=True)
    @testing.numpy_cupy_allclose(rtol=1e-4, atol=1e-7, accept_error=ValueError,
                                 contiguous_check=False, scipy_name='scp')
    def test_rfft(self, xp, scp, dtype):
        x = testing.shaped_random(self.shape, xp, dtype)
        x_orig = x.copy()
        out = scp.fftpack.rfft(x, n=self.n, axis=self.axis)
        testing.assert_array_equal(x, x_orig)
        return out

    @testing.for_all_dtypes(no_complex=True)
    @testing.numpy_cupy_allclose(rtol=1e-4, atol=1e-7, accept_error=ValueError,
                                 contiguous_check=False, scipy_name='scp')
    def test_rfft_overwrite(self, xp, scp, dtype):
        x = testing.shaped_random(self.shape, xp, dtype)
        return scp.fftpack.rfft(x, n=self.n, axis=self.axis,
                                overwrite_x=True)

    @testing.for_all_dtypes(no_complex=True)
    @testing.numpy_cupy_allclose(rtol=1e-4, atol=1e-7, accept_error=ValueError,
                                 contiguous_check=False, scipy_name='scp')
    def test_irfft(self, xp, scp, dtype):
        x = testing.shaped_random(self.shape, xp, dtype)
        x_orig = x.copy()
        out = scp.fftpack.irfft(x, n=self.n, axis=self.axis)
        testing.assert_array_equal(x, x_orig)
        return out

    @testing.for_all_dtypes(no_complex=True)
    @testing.numpy_cupy_allclose(rtol=1e-4, atol=1e-7, accept_error=ValueError,
                                 contiguous_check=False, scipy_name='scp')
    def test_irfft_overwrite(self, xp, scp, dtype):
        x = testing.shaped_random(self.shape, xp, dtype)
        return scp.fftpack.irfft(x, n=self.n, axis=self.axis,
                                 overwrite_x=True)

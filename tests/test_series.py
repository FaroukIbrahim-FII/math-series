from math_series import __version__
from math_series.series import fibonacci, lucas, sum_series

def test_version():
    assert __version__ == '0.1.0'


def test_fibonacci_5():
    expected = 5
    actual = fibonacci(5)
    assert actual == expected

def test_lucas_5():
    expected = 11
    actual = lucas(5)
    assert actual == expected

def test_sum_series_5_fib():
    expected = 5
    actual = sum_series(5)
    assert actual == expected

def test_sum_series_5_lucas():
    expected = 11
    actual = sum_series(5,2,1)
    assert actual == expected
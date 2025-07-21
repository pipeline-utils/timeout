import time

import pytest

from timeout import TimeoutException, timeout_decorator


def test_timeout_decorator():
    @timeout_decorator(1)
    def long_running_function():
        time.sleep(2)

    with pytest.raises(TimeoutException):
        long_running_function()


def test_timeout_decorator_with_args_and_return_value():
    @timeout_decorator(1)
    def long_running_function_with_kwargs(arg1, arg2=None):
        time.sleep(2)

    with pytest.raises(TimeoutException):
        long_running_function_with_kwargs("arg1", arg2="arg2")


def test_timeout_decorator_without_exception():
    @timeout_decorator(1)
    def short_running_function():
        time.sleep(0.5)
        return "finished"

    try:
        result = short_running_function()
    except TimeoutException:
        pytest.fail("TimeoutException was raised unexpectedly")
    assert result == "finished"

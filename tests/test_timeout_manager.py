import time

import pytest

from timeout import TimeoutException, timeout_manager


def test_timeout_manager():
    with pytest.raises(TimeoutException):
        with timeout_manager(1):
            time.sleep(2)


def test_timeout_manager_no_exception():
    try:
        with timeout_manager(1):
            time.sleep(0.5)
    except TimeoutException:
        pytest.fail("TimeoutException raised unexpectedly")


def test_timeout_manager_custom_exception():
    class CustomException(TimeoutException):
        pass

    with pytest.raises(CustomException):
        with timeout_manager(1, exception=CustomException):
            time.sleep(2)


def test_timeout_manager_custom_exception_no_exception():
    class CustomException(TimeoutException):
        pass

    try:
        with timeout_manager(1, exception=CustomException):
            time.sleep(0.5)
    except CustomException:
        pytest.fail("CustomException raised unexpectedly")

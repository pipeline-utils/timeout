import signal
from contextlib import contextmanager
from typing import Type


class TimeoutException(TimeoutError):
    """Custom exception for timeout errors."""


@contextmanager
def timeout_manager(
    seconds: int, message: str = "Operation timed out!", exception: Type[TimeoutException] = TimeoutException
):
    def signal_handler(signum, frame):
        raise exception(message)

    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)


def timeout_decorator(
    seconds: int, message: str = "Operation timed out!", exception: Type[TimeoutException] = TimeoutException
):
    """Decorator to apply a timeout to a function."""

    def decorator(func):
        def wrapper(*args, **kwargs):
            with timeout_manager(seconds, message, exception):
                return func(*args, **kwargs)

        return wrapper

    return decorator


__all__ = ["timeout_manager", "timeout_decorator", "TimeoutException"]

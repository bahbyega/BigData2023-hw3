import time
import logging
import functools


def backoff(tries=5, sleep=10):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(tries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    logging.error(f"Backoff attempt failed {i + 1}/{tries} times: {e}")
                    time.sleep(sleep)
            logging.error("Message processing error")

        return wrapper

    return decorator

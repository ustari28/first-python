import functools
from datetime import datetime


# security decorator for validating context security
def security(option):
    def validate(func):
        """View decorator that redirects anonymous users to the login page."""

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("Option", option)
            return func(*args, **kwargs)

        return wrapper

    return validate


# logging decorator for tracing requests
def logging(func):
    """View decorator that redirects anonymous users to the login page."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Starting time", datetime.now(), func.__name__)
        val = func(*args, **kwargs)
        print("Finishing time", datetime.now(), func.__name__)
        return val

    return wrapper


# Singleton decorator
class Singleton:
    def __init__(self, cls):
        self.cls = cls
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.cls(*args, **kwargs)
        return self.instance

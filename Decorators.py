import functools

from flask import request


# security decorator for validating context security
def security(option):
    def validate(func):
        """View decorator that redirects anonymous users to the login page."""

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("Option {}", option)
            return func(*args, **kwargs)
        return wrapper
    return validate


# logging decorator for tracing requests
def logging(func):
    """View decorator that redirects anonymous users to the login page."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Starting time {0}", func.__name__)
        val = func(*args, **kwargs)
        print("Finishing time %s", func.__name__)
        return val
    return wrapper


def serializable(cls):
    class wrapper:
        def __init__(self, *args):
            self.wrapped = cls(*args)

        def __getattr__(self, *args):
            return getattr(self.wrapped, *args)

        def serialize(self):
            return jsonpickle.encode(self.wrapped)

    @staticmethod
    def deserialize(ser_str):
        return jsonpickle.decode(ser_str)

    return wrapper

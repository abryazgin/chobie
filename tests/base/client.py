from django.test import Client
import functools



def __factory():
    """
    Client factory

    Returns:
        Instance of Django's Client
    """
    return Client()


def decorator(func):
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        client = __factory()
        return func(client, *args, **kwargs)
    return wrap


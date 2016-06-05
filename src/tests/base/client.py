import functools

from django.test import Client
import config


def factory():
    """
    Client factory

    Returns:
        Instance of Django's Client
    """
    return Client()


def decorator(func):
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        client = factory()
        return func(client, *args, **kwargs)
    return wrap


def openurl(client, suburl):
    return client.get('{domain}{suburl}'.format(domain=config.url, suburl=suburl))

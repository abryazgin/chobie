from tests.base import webdriver, client
from tests.base.factory import user


def before_all(context):
    """
    Action runs before all features in behave testing
    """
    start_browser_in_context(context, 'firefox')
    start_client_in_context(context)
    create_test_user()


def after_all(context):
    """
    Action runs after all features in behave testing
    """
    try:
        context.browser.quit()
    finally:
        remove_test_user()


def start_browser_in_context(context, webdriver_name):
    print('Opening {} browser ...'.format(webdriver_name.title()))
    context.browser = webdriver.factory(webdriver_name)
    print('Browser {} opened!'.format(webdriver_name.title()))


def start_client_in_context(context):
    context.client = client.factory()


def stop_browser_in_context(context, webdriver_name):
    print('Close {} browser ...'.format(webdriver_name.title()))
    context.browser.quit()
    print('Browser {} closed!'.format(webdriver_name.title()))


def create_test_user():
    user.create_fake_user()


def remove_test_user():
    user.remove_fake_user()



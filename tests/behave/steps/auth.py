from behave import *

from tests.base.webdriver import NoSuchElementException, goto
from tests.base.factory import user
from tests.base.utils import randomizer


def login(context, username, password):
    goto(context.browser, '/login/')

    context.browser.find_element_by_id("id_username").send_keys(username)
    context.browser.find_element_by_id("id_password").send_keys(password)
    context.browser.find_element_by_xpath('//input[@value="login"]').click()


def is_error(context):
    try:
        if context.browser.find_element_by_name("error"):
            return True
    except NoSuchElementException:
        return False


def is_success(context):
    return not is_error(context)


@given(u'I am a some registered user')
def step_impl(context):
    context.user = {
        'username': user.fake_username,
        'password': user.fake_password
    }


@given(u'I am a some unregistered user')
def step_impl(context):
    context.user = {
        'username': randomizer.rndstring(10),
        'password': randomizer.rndstring(10)
    }


@when(u'I try login')
def step_impl(context):
    login(context, context.user['username'], context.user['password'])


@when(u'I try login with incorrect password')
def step_impl(context):
    login(context, context.user['username'], randomizer.rndstring(10))


@then(u'I succesfully login')
def step_impl(context):
    is_success(context)


@then(u"I don't login")
def step_impl(context):
    is_error(context)

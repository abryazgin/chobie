from behave import *

from tests.base.webdriver import NoSuchElementException, openurl as wd_openurl, checkurl
from tests.base.client import openurl as cl_openurl


def is_error(context):
    try:
        if context.browser.find_element_by_name("error"):
            return True
    except NoSuchElementException:
        return False


def is_success(context):
    return not is_error(context)


def goto(context, suburl):
    if hasattr(context, 'browser'):
        wd_openurl(context.browser, suburl)
    if hasattr(context, 'client'):
        context.response = cl_openurl(context.client, suburl)


def getstatus(context):
    return context.response.status_code


@when(u"I go to '{suburl}'")
def step_impl(context, suburl):
    goto(context, suburl)


@then(u"I have redirected to '{page}' page")
def step_impl(context, page):
    suburl = '/{page}/'.format(page=page)
    checkurl(context.browser, suburl)


@then(u"Success")
def step_impl(context):
    assert 200 <= getstatus(context) < 300


@then(u"Redirected")
def step_impl(context):
    assert 300 <= getstatus(context) < 400


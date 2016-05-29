#! -*-coding:utf-8-*-
from behave import *


'''
GIVEN
'''


@given('Nothing')
def step_impl(context):
    pass


@given(u'У нас есть steps с русскими символами')
def step_impl(context):
    pass


'''
WHEN
'''


@when('Run a passing step')
def step_impl(context):
    pass


@when(u'Когда мы запускаем какой-нибудь из них')
def step_impl(context):
    assert True is not False


'''
THEN
'''


@then('Everything is fine')
def step_impl(context):
    assert context.failed is False


@then(u'Ничего не ломается!')
def step_impl(context):
    assert context.failed is False

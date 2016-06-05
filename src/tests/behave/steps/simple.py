#! -*-coding:utf-8-*-
from behave import *


'''
GIVEN
'''


@step(u'Nothing')
def step_impl(context):
    pass


@given(u'У нас есть steps с русскими символами')
def step_impl(context):
    pass


'''
WHEN
'''


@when(u'Run a passing step')
def step_impl(context):
    pass


@when(u'Когда мы запускаем какой-нибудь из них')
def step_impl(context):
    assert True is not False


'''
THEN
'''


@then(u'Everything is fine')
def step_impl(context):
    assert True is not False


@then(u'Ничего не ломается!')
def step_impl(context):
    assert True is not False

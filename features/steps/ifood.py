from behave import *
from behave_webdriver.steps import *

@given('I am on ifood page "{url}"')
def step(context, url)
    context.browser.get(url)

@when('I type my address')
def step(context)
    elem = context.browser.find_element_by_class('.address-search-input__field')
    elem.sendKeys('Jaragua do Sul')
    elem.submit()

@then('My location should be shown on the modal')
def step(context)
    addressList = context.browser.find_element_by_class('.address-search-list')
    assert addressList in context.browser.page_source
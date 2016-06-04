from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException # For using in other modules

import os
import config


def factory(webdriver_name):
    """
    Webdriver factory
    Args:
        webdriver_name: on of this 'android', 'blackberry', 'chrome', 'firefox', 'ie', 'safari', etc.

    Returns:
        Instance of webdriver ("browser")
    """
    browser = getattr(webdriver, webdriver_name)
    return browser.webdriver.WebDriver()


def goto(webdriver, suburl):
    webdriver.get('{domain}{suburl}'.format(domain=config.url, suburl=suburl))

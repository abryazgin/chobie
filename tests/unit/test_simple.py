import unittest

from tests.base import client as clienter, webdriver


class TestBase(unittest.TestCase):

    @staticmethod
    @clienter.decorator
    def test_django_client_working(client):
        response = client.post('/login/', {'username': 'someuser', 'password': 'somepass'})
        assert response is not None

    @staticmethod
    def test_import_models_from_polls():
        polls = __import__('polls')
        assert polls.models.Role is not None
        assert polls.models.Scope is not None
        assert polls.models.UserScope is not None

    @staticmethod
    def test_selenium_webdriver():
        browser = webdriver.factory('firefox')

        assert browser is not None
        browser.get('http://127.0.0.1:8000/login/')
        username_input = browser.find_element_by_name("username")
        username_input.send_keys('myuser')
        password_input = browser.find_element_by_name("password")
        password_input.send_keys('secret')
        browser.find_element_by_xpath('//input[@value="login"]').click()
        assert browser.current_url is not None

        browser.quit()


if __name__ == '__main__':
    unittest.main()

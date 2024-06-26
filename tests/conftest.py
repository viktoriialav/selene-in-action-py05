import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    # browser.config.base_url = 'https://todomvc.com/examples/emberjs'
    browser.config.base_url = 'https://todomvc-emberjs-app.autotest.how'
    browser.config.timeout = 2.0
    # browser.config.driver_name = 'firefox'
    driver_options = webdriver.FirefoxOptions()
    driver_options.add_argument('--headless')
    browser.config.driver_options = driver_options

    yield

    browser.quit()

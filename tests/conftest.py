import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    # browser.config.base_url = 'https://todomvc.com/examples/emberjs'
    browser.config.base_url = 'https://todomvc-emberjs-app.autotest.how'
    browser.config.timeout = 2.0
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless')
    browser.config.driver_options = driver_options
    # Create your own driver for browser
    browser.config.driver = webdriver.Chrome(
        service=ChromService(executable_path=ChromeDriverManager().install()),
        options=driver_options,
    )

    # # for Yandex browser
    # yandex_driver_file = r'F:\Drivers\yandexdriver.exe'
    # browser.config.driver = webdriver.Chrome(
    #     service=ChromService(executable_path=yandex_driver_file),
    #     options=driver_options,
    # )

    yield

    browser.quit()

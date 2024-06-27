import pytest
from selene import browser as selene_browser, Browser, Config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    # browser.config.base_url = 'https://todomvc.com/examples/emberjs'
    selene_browser.config.base_url = 'https://todomvc-emberjs-app.autotest.how'
    selene_browser.config.timeout = 2.0
    selene_browser.config.type_by_js = True
    driver_options = webdriver.ChromeOptions()
    # driver_options.add_argument('--headless')
    selene_browser.config.driver_options = driver_options
    # Create your own driver for browser
    selene_browser.config.driver = webdriver.Chrome(
        service=ChromService(executable_path=ChromeDriverManager().install()),
        options=driver_options,
    )

    '''
    # for Yandex browser
    yandex_driver_file = r'F:\Drivers\yandexdriver.exe'
    browser.config.driver = webdriver.Chrome(
        service=ChromService(executable_path=yandex_driver_file),
        options=driver_options,
    )
    '''

    yield

    selene_browser.quit()


@pytest.fixture()
def driver():
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless')
    driver = webdriver.Chrome(
        service=ChromService(executable_path=ChromeDriverManager().install()),
        options=driver_options,
    )

    yield driver

    driver.quit()


@pytest.fixture()
def browser(driver):

    yield Browser(Config(driver=driver))

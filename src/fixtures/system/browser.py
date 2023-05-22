from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options
import pytest
import logging


@pytest.fixture()
def selenium(pytestconfig):
    options = Options()
    browser_name = pytestconfig.getini("browser_name")
    logging.info(f'Подготовка {browser_name} браузера...')
    if pytestconfig.getini("headless") == "True" and browser_name == "chrome":
        options.add_argument("--headless")
    driver = Remote(
        desired_capabilities={
            "browserName": pytestconfig.getini("browser_name"),
            "browserVersion": pytestconfig.getini("browser_version")
        },
        command_executor=pytestconfig.getini("selenium_url"),
        options=options
    )
    driver.implicitly_wait(15)  # добавить неявное ожидание в 15 секунд
    logging.info(f'Браузер {browser_name} запущен.')
    yield driver
    driver.quit()

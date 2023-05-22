import logging.config
from os import path

log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.ini')
logging.config.fileConfig(log_file_path)

pytest_plugins = [
    "autotests_githab_skillbox.src.fixtures"
]


def pytest_addoption(parser):
    parser.addini("selenium_url", "Selenium Hub Url")
    parser.addini("browser_name", "Browser name for tests")
    parser.addini("browser_version", "Browser version for tests")
    parser.addini("headless", "Run browser in headless mode")

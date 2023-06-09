import os

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.quit()
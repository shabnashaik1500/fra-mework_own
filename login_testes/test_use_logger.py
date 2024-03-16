import time

from selenium import webdriver
import logging
def test_logging():
    Logger=logging.getLogger(__name__)
    driver=webdriver.Chrome()
    driver.get("https://google.com")
    driver.maximize_window()
    Logger.info(driver.title)
    time.sleep(5)
    driver.quit()
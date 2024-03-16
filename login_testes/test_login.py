import time
import pytest
from selenium import webdriver

def test_open_login():
    driver=webdriver.Chrome()
    driver.get("https://google.com")
    #driver.maximize_window()
    print(driver.title)
    time.sleep(5)
    driver.quit()
def test_open_login_Edge():
    driver=webdriver.Edge()
    driver.get("https://google.com")
    #driver.maximize_window()
    print(driver.title)
    time.sleep(5)
    driver.quit()
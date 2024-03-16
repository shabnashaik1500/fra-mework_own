import time

from selenium import webdriver
def test_login():
    driver=webdriver.Chrome()
    driver.get("https://google.com")
    driver.maximize_window()
    driver.back()
    driver.get("https://bingo.com")
    driver.forward()
    driver.refresh()
    driver.back()
    time.sleep(15)
    driver.quit()

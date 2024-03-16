import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os
def test_nopcommerse():
    driver=webdriver.Chrome()
    driver.get("https://demo.nopcommerce.com/")
    driver.maximize_window()
    reg_link=Keys.CONTROL+Keys.ENTER
    driver.find_element(By.LINK_TEXT,"Register").send_keys(reg_link)
    time.sleep(5)
    driver.quit()
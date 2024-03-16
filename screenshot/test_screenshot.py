from selenium import webdriver
from selenium.webdriver.common.by import By
import os
def test_nopcommerse():
    driver=webdriver.Chrome()
    driver.get("https://demo.nopcommerce.com/")
    driver.maximize_window()
    #driver.save_screenshot("C:\\Users\\esita\\PycharmProjects\\selenium_practice\\screenshot\\fullpage.png")
    driver.save_screenshot(os.getcwd()+"\\homepage.png")
    driver.quit()
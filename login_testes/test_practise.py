import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
def test_waits():
    driver=webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
    list_of_elements=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains (@id,'day')]")
    for i in list_of_elements:
        if i=="sunday" or i=="monday":
             i.click()
    time.sleep(15)
    driver.quit()

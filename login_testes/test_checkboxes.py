import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_checkboxes():
    driver=webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
    click_on_checkbox=driver.find_element(By.XPATH,"//input[@id='sunday']").click()
    list_of_elements_clickable=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
    #for i in list_of_elements_clickable:
     #   i.click()
      #  time.sleep(10)
    for i in list_of_elements_clickable:
        weekname=i.get_attribute("id")
        if weekname=="sunday" or weekname=="monday":
            i.click()
    time.sleep(10)

    driver.quit()
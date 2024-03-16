import time

from selenium import webdriver
from selenium.webdriver.common.by import By
def test_open_login_using_xpath_functions():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    #driver.maximize_window()
    #using contains
    make_apointment=driver.find_element(By.XPATH,"//a[contains(text(),'Make')]").click()
    #or
    #make_appointment=driver.find_element(By.XPATH,"//a[contains(text(),'Appointment')]").click()
    #using starts-with
    #make_appointment=driver.find_element(By.XPATH,"//a[starts-with(text(),'Make')]").click()
    time.sleep(5)
    driver.quit()

def test_open_login_using_xpath_functions():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    #driver.maximize_window()
    # using contains
    make_apointment = driver.find_element(By.XPATH, "//a[contains(text(),'Make')]").click()
        # or
    # make_appointment=driver.find_element(By.XPATH,"//a[contains(text(),'Appointment')]").click()
    # using starts-with
    #make_appointment = driver.find_element(By.XPATH, "//a[starts-with(text(),'Make')]").click()
    time.sleep(5)
    driver.quit()


import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_open_login():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    #driver.find_element(By.ID,"btn-make-appointment").click()
    #driver.find_element(By.PARTIAL_LINK_TEXT,"Make").click()
    driver.find_element(By.LINK_TEXT,"Make Appointment").click()
    print(driver.current_url)
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/profile.php#login","error message"
    username=driver.find_element(By.ID,"txt-username").send_keys("John Doe")
    password=driver.find_element(By.ID,"txt-password").send_keys("ThisIsNotAPassword")
    login_button=driver.find_element(By.ID,"btn-login").click()
    time.sleep(5)
    driver.quit()
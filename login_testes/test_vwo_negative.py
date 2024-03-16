import time

from selenium import webdriver
from selenium.webdriver.common.by import By
def test_open_login():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    driver.maximize_window()
    username=driver.find_element(By.ID,"login-username").send_keys("admin")
    password=driver.find_element(By.ID,"login-password").send_keys("admin")
    login_btn=driver.find_element(By.ID,"js-login-btn").click()
    verified_msg=driver.find_element(By.ID,"js-notification-box-msg")
    time.sleep(5)
    assert verified_msg.text=="Your email, password, IP address or location did not match","error message"
    time.sleep(5)
    driver.quit()

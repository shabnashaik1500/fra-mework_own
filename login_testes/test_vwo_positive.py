import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_open_login():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    driver.maximize_window()
    username=driver.find_element(By.XPATH,"//input[@id='login-username']").send_keys("contact+atb5x@thetestingacademy.com")
    password=driver.find_element(By.XPATH,"//input[@id='login-password']").send_keys("ATBx@1234")
    submit_btn=driver.find_element(By.XPATH,"//button[@id='js-login-btn']").click()
    WebDriverWait(driver,20).until(
        EC.text_to_be_present_in_element((By.XPATH,"//h1[@data-qa='page-heading']"),"Dashboard")
    )
    #time.sleep(20)
    heading_msg=driver.find_element(By.XPATH,"//span[@data-qa='lufexuloga']")
    assert heading_msg.text=="Aman"
    time.sleep(30)
    driver.quit()

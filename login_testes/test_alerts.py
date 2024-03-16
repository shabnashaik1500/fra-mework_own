from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def test_alert():
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()
    #click_on_alert=driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']").click()
    #click_on_confirm=driver.find_element(By.XPATH,"//button[@onclick='jsConfirm()']").click()
    click_on_prompt=driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']")
    click_on_prompt.click()
    WebDriverWait(driver,10).until(EC.alert_is_present())
   # alert=driver.switch_to.alert
    #alert.accept()
    #alert=driver.switch_to.alert
    #alert.accept()
    alert=driver.switch_to.alert
    alert.send_keys("shabna")
    alert.accept()
    result=driver.find_element(By.XPATH,"//p[@id='result']")
    print(result.text)
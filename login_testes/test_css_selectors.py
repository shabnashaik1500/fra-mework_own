from selenium import webdriver
from selenium.webdriver.common.by import By
def test_make_appointment():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    make_appointment=driver.find_element(By.CSS_SELECTOR,"a[id='btn-make-appointment']").click()
    driver.quit()
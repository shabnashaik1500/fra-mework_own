import time

from selenium import webdriver
from selenium.webdriver.common.by import By
def test_open_google():
    driver=webdriver.Chrome()
    driver.get("https://google.com")
    driver.maximize_window()
    text_box=driver.find_element(By.XPATH,"//textarea[@aria-controls='Alh6id']")
    text_box.send_keys("selenium")
    text_box.submit()
    time.sleep(10)
    driver.quit()

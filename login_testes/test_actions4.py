import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
def test_actions():
    driver=webdriver.Chrome()
    driver.get("https://www.makemytrip.com/")
    country_code=driver.find_element(By.ID,"fromCity")
    actions=ActionChains(driver)
    actions.move_to_element(country_code).click().send_keys("Mumbai").perform()
    time.sleep(5)
    driver.quit()
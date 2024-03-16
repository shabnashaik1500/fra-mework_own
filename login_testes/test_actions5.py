import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
def test_actions():
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/windows")
    parent_window=driver.find_element(By.LINK_TEXT,"Click Here")
    actions=ActionChains(driver)
    #actions.move_to_element(parent_window).click().perform()
    actions.click(parent_window).perform()
    time.sleep(5)
    driver.quit()
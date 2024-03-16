import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
def test_actions():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    #clickable=driver.find_element(By.XPATH,"//input[@id='clickable']")
    #click_hold=driver.find_element(By.XPATH,"//a[@id='click']")
    actions=ActionChains(driver)
    #actions.key_down(Keys.SHIFT).send_keys_to_element(clickable,"shabna").key_up(Keys.SHIFT).perform()
    #actions.click_and_hold(clickable).key_down(Keys.SHIFT).send_keys("shabna").key_up(Keys.SHIFT).perform()
    #actions.click_and_hold(click_hold).perform()
    #actions.click(click_hold).perform()
    actions.double_click(clickable).perform()
    time.sleep(5)
    driver.quit()

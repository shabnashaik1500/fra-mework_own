import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
def test_actions():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    click_hover=driver.find_element(By.XPATH,"//input[@id='hover']")
    actions=ActionChains(driver)
    actions.move_to_element(click_hover).perform()
    time.sleep(5)
    driver.quit()
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
def test_actions():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    draggable=driver.find_element(By.XPATH,"//div[@id='draggable']")
    droppable=driver.find_element(By.XPATH,"//div[@id='droppable']")
    actions=ActionChains(driver)
    actions.drag_and_drop(draggable,droppable).perform()
    time.sleep(5)
    driver.quit()

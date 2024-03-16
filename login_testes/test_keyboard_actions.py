import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
def test_keyboard_actions():
    driver=webdriver.Chrome()
    driver.get("https://text-compare.com/")
    first_box=driver.find_element(By.XPATH,"//textarea[@id='inputText1']").send_keys("Welcome to Selenium")
    second_box=driver.find_element(By.XPATH,"//textarea[@id='inputText2']")
    actions=ActionChains(driver)
    actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
    actions.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
    actions.send_keys(Keys.TAB).perform()
    actions.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
    time.sleep(5)
    driver.quit()
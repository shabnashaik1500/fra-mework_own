#actions are used for mouse and keyboard actions
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
def test_actions():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    first_name=driver.find_element(By.NAME,"firstname")
   # check_box=driver.find_element(By.ID,"sex-0").click()
   # result=driver.find_element(By.LINK_TEXT,"Click here to Download File")
    actions=ActionChains(driver)
    actions.key_down(Keys.SHIFT).send_keys_to_element(first_name,"shabna").key_up(Keys.SHIFT).perform()
    #actions.perform()
    #actions.context_click(result).perform()
    time.sleep(10)
    driver.quit()
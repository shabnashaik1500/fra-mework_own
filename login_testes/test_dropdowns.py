import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
def test_dropdowns():
    driver=webdriver.Chrome()
    driver.get("https://www.opencart.com/index.php?route=account/register")
    driver.maximize_window()
    time.sleep(10)
    country_code=driver.find_elements(By.XPATH,"//select[@id='input-country']")
    for country in country_code:
        country.is_selected("India")

    #country_code.select_by_visible_text("Angola")
    time.sleep(15)
    driver.quit()
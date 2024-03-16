import time

from selenium import webdriver
def test_chrome_options():
    chrome_options=webdriver.ChromeOptions()
    driver=webdriver.Chrome(options=chrome_options)
    driver.get("https://google.com")
    driver.maximize_window()
    driver.back()

    driver.refresh()
    time.sleep(20)
    #driver.close()
    driver.quit()
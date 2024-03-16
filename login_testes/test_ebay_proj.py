from selenium import webdriver
from selenium.webdriver.common.by import By
def test_ebay_proj():
    driver=webdriver.Chrome()
    driver.get("https://www.ebay.com/")
    driver.maximize_window()
    search_items=driver.find_element(By.XPATH,"//input[@type='text']").send_keys("16gb")
    click_search=driver.find_element(By.XPATH,"//input[@id='gh-btn']").click()
    list_of_items=driver.find_elements(By.XPATH,"//span[@role='heading']")
    for i in list_of_items:

        print(i.text)
    driver.quit()
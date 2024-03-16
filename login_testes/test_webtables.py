from selenium import webdriver
from selenium.webdriver.common.by import By

def test_webtables():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable.html")
    driver.maximize_window()
    row_elements=driver.find_elements(By.XPATH,"//table[@id='customers']/tbody/tr")
    print(len(row_elements))
    col_elements=driver.find_elements(By.XPATH,"//table[@id='customers']/tbody/tr[2]/td")
    print(len(col_elements))
    print_ronalds_contact=driver.find_element(By.XPATH,"//table[@id='customers']/tbody/tr[4]/td[2]")
    print(print_ronalds_contact.text)
    ronalds_country=driver.find_element(By.XPATH,"//table[@id='customers']/tbody/tr[4]/td[2]/following-sibling::td")
    print(ronalds_country.text)

    driver.quit()
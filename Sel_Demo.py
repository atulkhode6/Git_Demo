from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_option=Options()
chrome_option.add_experimental_option("detach",True )

driver=webdriver.Chrome(options=chrome_option)

driver.get("http://www.google.com")

driver.find_element(By.XPATH,"//*[@id='APjFqb']").send_keys('selenium')

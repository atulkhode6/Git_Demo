import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=chrome_options)

chr = Options()
chr.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chr)




driver.maximize_window()
driver.get("https://www.opera.com/?utm_campaign=%2307%20-%20IN%20-%20Search%20-%20EN%20-%20Branded%20-%202017&utm_content=40191622276&gclid=CjwKCAjwmbqoBhAgEiwACIjzEMqHlC834XnGCC4lvRH9jcIVu-Ces-fnzKzVpSaU7l-z6zjBOQPpqBoCZncQAvD_BwE")
time.sleep(2)
ele=driver.find_element(By.XPATH,"//span[@class='btn width-100 btn--primary cookie-consent__btn cookie-basic-consent__btn']")
print(ele.text)
ele.click()

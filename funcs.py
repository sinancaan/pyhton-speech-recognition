import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

driver_path = "/Users/sinancan/selenium/chromedriver"
driver = webdriver.Chrome(executable_path="chromedriver")


def websitesine_gir(link):
    driver.get(f"https://{link}")
    driver.maximize_window()
    time.sleep(5)

def ara(obj):

    driver.get('http://www.google.com')

    search = driver.find_element(By.NAME, 'q')
    search.send_keys(obj)
    search.send_keys(Keys.RETURN)  # hit return after you enter search text
    time.sleep(5)  # sleep for 5 seconds so you can see the results
    driver.quit()

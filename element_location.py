# LOCATORS: ID, NAME, XPATH, CLASS_NAME, LINK_TEXT, PARTIAL_LINK_TEXT, CSS_SELECTOR

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# initialize web browser
driver = webdriver.Chrome()

# test scenario starts
driver.get("http://automationpractice.com/index.php")
time.sleep(5)

search_box = driver.find_element(By.NAME, 'search_query')
#search_box = driver.find_element(By.ID, 'search_query_top')
#search_box = driver.find_element(By.CSS_SELECTOR, 'search_query')
search_box.send_keys("dress")
time.sleep(5)

# clicking the search button, finding by XPATH
# "//tag[@attribute='valueofattribute' and @attribute2='value2']"
# "//div/div/form/input[@type='submit']"
search_box = driver.find_element(By.XPATH, "//button[@name='submit_search']").click()

#search_box = driver.find_element(By.CSS_SELECTOR, 'button.button-search').click()

time.sleep(5)

# click the sign in button
driver.find_element(By.PARTIAL_LINK_TEXT, 'Sign in').click()
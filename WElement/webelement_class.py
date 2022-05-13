# Chapter 4: web element properties and methods

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def initialize_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    return driver

def webelement_properties(driver):
    driver.get("http://automationpractice.com")
    time.sleep(10)

    # finding the multiple element
    product_names = driver.find_elements(By.XPATH, "//a[@title='Add to cart']")
    #print(len(product_names))
    time.sleep(1)

    print("using the webelement properties for each element")
    for prod_name in product_names:
        print("cart_button.text: ", prod_name.text)
        print("cart_button.size: ", prod_name.size)
        print("cart_button.tag_name: ", prod_name.tag_name)

def close_browser(driver):
    print(" closing the whole browser")
    time.sleep(3)
    driver.quit()

def webelement_methods(driver):
    #driver = webdriver.Chrome()
    #driver.implicitly_wait(20)

    #open website
    driver.get("http://automationpractice.com")

    #enter 'dress' in the search box, wait 5 sec
    search_box = driver.find_element(By.ID, 'search_query_top')
    search_box.send_keys('selenium')
    #search_box.send_keys('selenium' + Keys.ENTER)
    time.sleep(5)

    #clear search box and enter 'dress'
    search_box.clear()
    search_box.send_keys('dress')

    #click search button
    # driver.find_element(By.NAME, 'submit_search').click()
    search_button = driver.find_element(By.NAME, 'submit_search')
    search_button.click()

    #verify compare button is displayed
    compare_btn = driver.find_element(By.XPATH, '//form[@class="compare-form"]')
    print("compare_btn.is.displayed():, ", compare_btn.is_displayed())
    #assert compare_btn.is_displayed()

    #verify compare button is not enabled
    print("compare_btn.is.enabled():, ", compare_btn.is_enabled())

    #get attribute 'action' of compare
    print("action attribute of compare form: ", compare_btn.get_attribute('action'))


def test_explicit_wait():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(20)

    # time object from WebDriverWait()
    # you need list of conditions from expected_conditions() class

    url = "https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver"
    webdriver_wait = WebDriverWait(driver, 30)

    # open the website
    print("#######  test explicit wait start #######")
    driver.get(url)

    # get the initial text

    # OPTION 1
    # original_msg = driver.find_element(By.ID, 'h2').text

    # OPTION 2
    original_msg = webdriver_wait.until((EC.presence_of_element_located(By.ID, 'h2'))).text
    print(f"original message displayed: {original_msg}")

    # click in "Change Text to "Selenium Webdriver" button
    driver.find_element(By.ID, 'populate-text').click()

    # wait until text is present in the element "Selenium Webdriver", max wait time is 20
    webdriver_wait.until(EC.text_to_be_present_in_element((By.ID, "h2"), "Selenium"))
    target_msg = driver.find_element(By.ID, 'h2').text
    print(f"target message: {target_msg}")



    print("###### element_to_be_clickable ######")
    print("check if button is enabled if not click on 'Enable button after 10 seconds'")
    print(f"checking the button: {driver.find_element(By.ID, 'disable').is_enabled()}")

    if not driver.find_element(By.ID, 'disable').is_enabled():
        driver.find_element(By.ID, 'enable-button').click()

    print("wait until Button is enabled, then click the button")
    webdriver_wait.until(EC.element_to_be_clickable((By.ID, 'disable')))
    driver.find_element(By.ID, 'disable').click()
    print("###### element_to_be_clickable ######")

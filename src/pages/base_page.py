from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        driver = webdriver.Chrome()
        self.driver = driver
        self.webdriver_wait = WebDriverWait(driver, 10)

    def click_element_by_id(self, id):
        try:
            element = self.webdriver_wait.until(EC.presence_of_element_located((By.Id, id)))
            element.clear()
            element.send_keys()

        except(NoSuchElementException, TimeoutException) as err:
            print(f"error in click element by id, please check id='{id}")
            print(f"error: {err}")

    def click_element_by_xpath(self, xpath):
        try:
            element = self.webdriver_wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            element.clear()
            element.send_keys()

        except(NoSuchElementException, TimeoutException) as err:
            print(f"error in click element by id, please check xpath='{xpath}")
            print(f"error: {err}")

    def click_element_by_name(self, name):
        try:
            element = self.webdriver_wait.until(EC.presence_of_element_located((By.NAME, name)))
            element.clear()
            element.send_keys()

        except(NoSuchElementException, TimeoutException) as err:
            print(f"error in click element by id, please check name='{name}")
            print(f"error: {err}")

    def enter_text_by_id(self, id, text):
        try:
            #element = self.driver.find_element(By.ID, id)
            element = self.webdriver_wait.until(EC.presence_of_element_located((By.ID, id)))
            element.send_keys(text)

        except(NoSuchElementException, TimeoutException) as err:
            print(f"error in click element by id, please check id='{id}")
            print(f"error: {err}")

    def select_from_dropdown_by_id_by_value(self, id, index_value):
        try:
            #element = self.driver.find_element(By.ID, id)
            element = self.webdriver_wait.until(EC.presence_of_element_located((By.ID, id)))
            selection = Select(element)  # find element with Select tagname
            selection.select_by_index(1)

        except(NoSuchElementException, TimeoutException) as err:
            print(f"error in click element by id, please check id='{id}' and index='{index_value}'")
            print(f"error: {err}")

    def is_element_selected_by_id(self, id):
        element = self.webdriver_wait.until(EC.presence_of_element_located((By.Id, id)))
        return  element.is_selected()

    def is_element_displayed_by_id(self, id):
        element = self.driver.find_element(By.ID, id)
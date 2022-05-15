from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Wdriver package, webdriver_class.py module
# WEDRIVER CLASS
driver = webdriver.Chrome()

class Abc():

    name = ''

    @property
    def title(self):
        return "this is the title"
    @property
    def title_xpath(self):
        return f"//div[@id='title-{self.name}']"

    def click_title(self, name):
        self.name = name
        driver.find_element(By.XPATH, self.title_xpath)

abc = Abc()
print(abc.title)
abc.click_title('dresses')
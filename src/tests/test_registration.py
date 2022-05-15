from src.steps.registration_steps import *

# VARIABLE



url = "http://automationpractice.com"
email = f"jdoe{time.strftime('%Y%m%d%H%M%S')}@mail.com"
first_name = 'John'
last_name = 'Doe'
password = '123456'

print("# test case steps here")
driver = initialize_browser('chrome')
open_website(driver, url)
open_registration_form(driver, email)
complete_registration_form(driver, first_name, last_name, password, email)

print("verify 'controller=order' in the url")
is_keyword_in_url(driver, 'controller=order')
close_browser()

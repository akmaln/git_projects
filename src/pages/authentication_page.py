import time

from src.pages.base_page import BasePage

class AuthenticationPage(BasePage):
    # locator
    __email_addr_id = 'email_create'
    __create_an_account_btn_id = 'SubmitCreate'
    __mr_title_id = 'id_gender1'
    __mrs_title_id = 'id_gender2'
    __password_id = 'passwd'


    # methods - that represent Actions on the page
    def enter_signup_email(self, email):
        print("entering the email address")
        self.enter_text_by_id(self.__email_addr_id, email)
        time.sleep(1)

    def click_create_account_button(self):
        print("clicking create an account button")
        self.click_element_by_id(self.__create_an_account_btn_id)
        time.sleep(2)

    def select_title(self, title):
        """selects the titls Mr. or Mrs."""
        if title.loer() == 'mr':
            print(f"select '{title}' radio button")
            self.click_element_by_id(self.__mr_title_id)
        else:
            self.click_element_by_id(self.__mrs_title_id)
        time.sleep(1)

    def get_title_selected(self):
        if self.is_element_selected_by_id(self.__mr_title_id):
            title_selected = 'Mr'
        elif self.is_element_selected_by_id(self.__mrs_title_id):
            title_selected = 'Mrs'
        else:
            title_selected = None
        return title_selected

    def enter_password(self, password):
        self.enter_text_by_id(self.__password_id, password)
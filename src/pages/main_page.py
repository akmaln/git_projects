from src.pages.base_page import BasePage


class MainPage(BasePage):
    # locators
    __signin_btn = '//a[@class="login"]'
    __search_box_id = 'search_query_top'
    __search_btn_name = 'submit_search'
    __cart_link_xpath = '//a[@title="View my shopping cart"]'


    # method
    def click_signin(self):
        "'clicks sign in link on the top menu'"
        self.click_element_by_xpath(self.signin_btn_xpath)

    def eneter_text_in_search(self, phrase):
        self.enter_text_by_id(self.__search_box_id, phrase)
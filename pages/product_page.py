from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_button.click()

    def should_be_product_add(self):
        assert self.is_element_present(*ProductPageLocators.ADD_PRODUCT_MESSAGE), "No message about adding to basket"
        book_name_in_message = self.browser.find_elements(*ProductPageLocators.ADD_PRODUCT_MESSAGE)[0].text
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        assert book_name == book_name_in_message, f"{book_name} in not in message {book_name_in_message}"

    def check_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert product_price == basket_price, f"Product price = {product_price}, basket price = {basket_price}."

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_PRODUCT_MESSAGE), (
               "Success message is presented, but should not be")

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ADD_PRODUCT_MESSAGE), (
               "Success message is presented, but should not be")
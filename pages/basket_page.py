from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "Products are in basket."
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), "Message about empty basket is not show."
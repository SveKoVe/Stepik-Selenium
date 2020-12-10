link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_button_add_to_basket(browser):
    browser.implicitly_wait(2)
    browser.get(link)
    buttons = browser.find_elements_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")

    assert len(buttons) == 1, f"Wrong number of buttons: {len(buttons)}."
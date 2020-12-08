import os

from selenium import webdriver
import time

try:
    # f = open('test.txt', 'w')
    # f.close()
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')

    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector('[name="firstname"]')
    input1.send_keys("Светлана")
    input2 = browser.find_element_by_css_selector('[name="lastname"]')
    input2.send_keys("Козлова")
    input3 = browser.find_element_by_css_selector('[name="email"]')
    input3.send_keys("e-mail")

    el = browser.find_element_by_id('file')
    el.send_keys(file_path)

    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
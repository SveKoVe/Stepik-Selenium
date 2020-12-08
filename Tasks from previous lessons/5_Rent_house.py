import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(browser, 12).until(
            expected_conditions.text_to_be_present_in_element((By.ID, "price"), '100')
        )
    button = browser.find_element_by_id('book')
    button.click()

    button = browser.find_element_by_id('solve')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    input_y = browser.find_element_by_id('answer')
    input_y.send_keys(y)

    button.click()

finally:
    time.sleep(10)
    browser.quit()
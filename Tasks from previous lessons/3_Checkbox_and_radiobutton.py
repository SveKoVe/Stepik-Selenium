from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
link_2 = "http://suninjuly.github.io/get_attribute.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    # Для link_2
    # x_element = browser.find_element_by_tag_name('img')
    # x = x_element.get_attribute('valuex')
    y = calc(x)

    input_y = browser.find_element_by_id('answer')
    input_y.send_keys(y)

    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()

    radio = browser.find_element_by_id('robotsRule')
    radio.click()

    button = browser.find_element_by_class_name('btn.btn-default')
    # scroll
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # people_radio = browser.find_element_by_id('peopleRule')
    # print(people_radio.get_attribute("checked"))

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
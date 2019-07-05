from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id("treasure")
x = x_element.get_attribute("valuex")
y = calc(x)

element_input = browser.find_element_by_id("answer")
element_input.send_keys(y)

check = browser.find_element_by_id("robotCheckbox")
check.click()

radio = browser.find_element_by_id("robotsRule")
radio.click()

btn = browser.find_element_by_class_name("btn-default")
btn.click()
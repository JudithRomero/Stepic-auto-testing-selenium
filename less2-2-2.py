from selenium import webdriver
import time
import math


browser = webdriver.Chrome()
#browser.execute_script("document.title='Script executing';alert('Robots at work');")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/execute_script.html"
browser.get(link)

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

browser.execute_script("window.scrollBy(0, 100);")

element_input = browser.find_element_by_id("answer")
element_input.send_keys(y)

check = browser.find_element_by_id("robotCheckbox")
check.click()

radio = browser.find_element_by_id("robotsRule")
radio.click()

button = browser.find_element_by_class_name("btn-default")
button.click()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

text = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR")
    )
nbutton = browser.find_element_by_css_selector('button.btn-primary').click()

x = browser.find_element_by_css_selector('#input_value').text

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)
inp = browser.find_element_by_css_selector('.form-control').send_keys(y)

button = browser.find_element_by_css_selector('button#solve').click()
from selenium import webdriver
import os 


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

name = browser.find_element_by_name("firstname")
name.send_keys("...")

surname = browser.find_element_by_name("lastname")
surname.send_keys("...")

email = browser.find_element_by_name("email")
email.send_keys("...")


files = browser.find_element_by_xpath("//input[@type='file']")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, '1.txt')
files.send_keys(file_path)

btn = browser.find_element_by_class_name("btn-primary")
btn.click()




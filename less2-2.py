from selenium import webdriver
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

num1 = browser.find_element_by_id("num1")
num2 = browser.find_element_by_id("num2")
x = num1.text
y = num2.text
summ = int(x) + int(y)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_visible_text(str(summ))

btn = browser.find_element_by_class_name("btn-default")
btn.click()

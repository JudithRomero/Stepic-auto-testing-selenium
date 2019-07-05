from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
element_name = browser.find_element_by_xpath("//input[@placeholder='Введите имя']")
element_surname = browser.find_element_by_xpath("//input[@placeholder='Введите фамилию']")
element_email = browser.find_element_by_xpath("//input[@placeholder='Введите Email']")

element_name.send_keys("Мой ответ")
element_surname.send_keys("Мой ответ")
element_email.send_keys("Мой ответ")
time.sleep(2)

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text

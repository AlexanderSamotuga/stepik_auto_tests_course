from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x,y):
  return str(x+y)
  
try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    value1 = ".nowrap#num1"
    value2 = ".nowrap#num2"
    value3 = "#dropdown"
    value4 = "button.btn.btn-default"
    
    # Ваш код, который заполняет обязательные поля
    
    x_element = browser.find_element(By.CSS_SELECTOR, value1)
    x = x_element.text
    y_element = browser.find_element(By.CSS_SELECTOR, value2)
    y = y_element.text
    
    select = Select(browser.find_element(By.CSS_SELECTOR, value3))
    select.select_by_value((calc(int(x),int(y)))) # ищем элемент с текстом "Python"
    
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, value4)
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
     # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций

    browser.close()
    time.sleep(2)
    browser.quit()

# не забываем оставить пустую строку в конце файла
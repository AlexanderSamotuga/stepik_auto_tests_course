from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    value1 = ".nowrap#input_value"
    value2 = ".form-check-input[type=\"checkbox\"]"
    value3 = ".form-check-label[for=\"robotsRule\"]"
    value4 = "#answer"
    # Ваш код, который заполняет обязательные поля
    
    x_element = browser.find_element(By.CSS_SELECTOR, value1)
    x = x_element.text
    y = calc(x)
    
    input1 = browser.find_element(By.CSS_SELECTOR, value4)
    input1.send_keys(str(y))
    
    option1 = browser.find_element(By.CSS_SELECTOR, value2)
    option1.click()

    option2 = browser.find_element(By.CSS_SELECTOR, value3)
    option2.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
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
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
  return math.log(abs(12*math.sin(x)))
  
try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    value1 = ".nowrap#input_value"
    value2 = ".form-control#answer"
    value3 = ".form-check-label[for='robotCheckbox']"
    value4 = ".form-check-label[for='robotsRule']"
    value5 = ".btn.btn-primary"
    
    # Ваш код, который заполняет обязательные поля
    
    x_element = browser.find_element(By.CSS_SELECTOR, value1)
    x = x_element.text
    
    # расчет и запись ответа
    y = calc(int(x))  
    input1 = browser.find_element(By.CSS_SELECTOR, value2)
    input1.send_keys(str(calc(int(x))))
    
    # Опции
    option1 = browser.find_element(By.CSS_SELECTOR, value3)
    browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
    option1.click()

    option2 = browser.find_element(By.CSS_SELECTOR, value4)
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()
    
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, value5)
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
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
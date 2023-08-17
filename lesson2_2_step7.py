from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import Select
import os 


  
try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    value1 = ".form-control[name=\"firstname\"]"
    value2 = ".form-control[name=\"lastname\"]"
    value3 = ".form-control[name=\"email\"]"
    value4 = "#file[name=\"file\"]"
    value5 = ".btn.btn-primary"
    
    # Ваш код, который заполняет обязательные поля
    
    input1 = browser.find_element(By.CSS_SELECTOR, value1)
    input1.send_keys("firstname")
    
    input2 = browser.find_element(By.CSS_SELECTOR, value2)
    input2.send_keys("lastname")
    
    input3 = browser.find_element(By.CSS_SELECTOR, value3)
    input3.send_keys("email")
    
    # расчет и запись ответа
    fileinput = browser.find_element(By.CSS_SELECTOR, value4)
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    fileinput.send_keys(file_path)
    
       
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
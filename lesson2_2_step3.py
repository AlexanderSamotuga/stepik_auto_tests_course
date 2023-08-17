from selenium import webdriver
import time



browser = webdriver.Chrome()
browser.execute_script("document.title='Script executing';alert('Robots at work');")
time.sleep(10)
    # закрываем браузер после всех манипуляций

browser.close()
time.sleep(2)
browser.quit()
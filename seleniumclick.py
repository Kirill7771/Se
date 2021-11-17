# Импортируем вебдрайв
from selenium import webdriver
  
# Создаем браузер
driver = webdriver.Firefox()
  
# Получить ссылку на олх
driver.get("https://www.olx.kz/")
  
# Получить элемент 
element = driver.find_element_by_link_text("Одежда")
  
# Клик по элементу
element.click()

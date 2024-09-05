from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import csv

driver = webdriver.Firefox()

url = 'https://www.divan.ru/category/krovati?in_stock=1&parameters%5B4%5D%5Bfrom%5D=160&parameters%5B4%5D%5Bto%5D=161&parameters%5B165%5D%5B%5D=3749'

driver.get(url)
time.sleep(5)

# Парсинг цен
prices = driver.find_elements(By.CLASS_NAME, 'ui-LD-ZU.KIkOH')

# Открытие CSV файла для записи
with open('prices_divan.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])

    # Записываем цены в CSV файл
    for price in prices:
        writer.writerow([price.text])


driver.quit()
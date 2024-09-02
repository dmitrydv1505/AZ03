import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import csv
import os


def main():
    while True:
        try:
            task = int(input("Выберите задание (1, 2 или 3): "))
            if task not in [1, 2, 3]:
                raise ValueError("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")

            if task == 1:
                task1()
            elif task == 2:
                task2()
            elif task == 3:
                task3()
            break

        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"Произошла ошибка: {e}")


def task1():
    # Параметры нормального распределения
    mean = 0  # Среднее значение
    std_dev = 1  # Стандартное отклонение
    num_samples = 1000  # Количество образцов

    # Генерация случайных чисел, распределенных по нормальному распределению
    data = np.random.normal(mean, std_dev, num_samples)

    # Построение гистограммы
    plt.hist(data, bins=30, edgecolor='black')
    plt.title('Гистограмма нормального распределения')
    plt.xlabel('Значение')
    plt.ylabel('Частота')
    plt.show()


def task2():
    # Генерация двух наборов случайных данных
    x = np.random.rand(100)
    y = np.random.rand(100)

    # Построение диаграммы рассеяния
    plt.scatter(x, y, alpha=0.5)
    plt.title('Диаграмма рассеяния')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()


def task3():
    try:
        url = 'https://www.divan.ru/category/divany'
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Примерный код для парсинга цен (может потребоваться корректировка в зависимости от структуры сайта)
        prices = [int(price.get_text(strip=True).replace(' ', '').replace('₽', ''))
                  for price in soup.find_all('div', class_='price')]

        # Запись данных в CSV
        with open('divan_prices.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Цена'])
            for price in prices:

                writer.writerow([price])

                    # Обработка данных
                if prices:
                    average_price = sum(prices) / len(prices)
                    print(f"Средняя цена: {average_price:.2f} рублей")
                    # Построение гистограммы цен
                    plt.hist(prices, bins=30, edgecolor='black')
                    plt.title('Гистограмма цен на диваны')
                    plt.xlabel('Цена')
                    plt.ylabel('Частота')
                    plt.show()
                else:
                    print("Не удалось найти цены на диваны.")

    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")

if __name__ == "__main__":
    main()
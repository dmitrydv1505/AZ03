import numpy as np
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
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
        # Отправляем запрос к сайту
        url = 'https://www.divan.ru/category/divany-i-kresla'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Находим все элементы с ценами
        prices = soup.find_all('span', {'class': 'ui-LD-ZU KIkOH', 'data-testid': 'price'})

        # Получаем только значения цен и переводим их в числовой формат
        prices = [int(price.text.replace(' ', '').replace('руб.', '')) for price in prices]

        # Создаем CSV файл с ценами
        df = pd.DataFrame(prices, columns=['Цена (руб)'])
        df.to_csv('prices.csv', index=False)

        # Находим среднюю цену на диваны
        avg_price = sum(prices) / len(prices)
        print(f'Средняя цена на диваны: {avg_price:.2f} руб')

        # Строим гистограмму цен
        plt.hist(prices, bins=20, color='skyblue', edgecolor='black')
        plt.xlabel('Цена (руб)')
        plt.ylabel('Количество')
        plt.title('Гистограмма цен на диваны')
        plt.grid(axis='y', alpha=0.75)
        plt.show()

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
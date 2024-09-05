import pandas as pd
import matplotlib.pyplot as plt


# Загрузка данных из CSV-файла
file_path = 'cleaned_prices_divan.csv'
data = pd.read_csv(file_path)


# Предположим, что столбец с ценами называется 'price'
prices = data['Price']
df = pd.DataFrame(prices)
print(f'Средняя цена кровати- {df['Price'].mean()}')

# Построение гистограммы
plt.hist(prices, bins=10, edgecolor='black')

# Мы можем изменить количество bin-ов по своему усмотрению


# Добавление заголовка и меток осей
plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Частота')


# Показать гистограмму
plt.show()
import numpy as np
import matplotlib.pyplot as plt

random_array_1 = np.random.rand(5)
random_array_2 = np.random.rand(5)

print(random_array_1, random_array_2)

plt.scatter(random_array_1, random_array_2)

plt.xlabel("Х")
plt.ylabel("Y")
plt.title("диаграмма рассеяния")

plt.show()
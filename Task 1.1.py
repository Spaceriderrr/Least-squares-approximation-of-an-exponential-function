import matplotlib.pyplot as plt
import numpy as np
import scipy


def func(x, b_0, b_1, b_2):
    return b_0 + b_1 * np.exp(-b_2 * x ** 2)


with open('x4.txt', 'rt', encoding='utf-8') as x_file, open('y4.txt', 'rt', encoding='utf-8') as y_file:
    x_points = list(map(float, x_file.read().split()))
    y_points = list(map(float, y_file.read().split()))

x_sum = sum(x_points)
y_sum = sum(y_points)

N = 50

a, b, c = scipy.optimize.curve_fit(func, xdata=x_points, ydata=y_points)[0]
print(f'Значення коефіцієнтів:\na={a}, b={b}, c={c}.\n')

plt.scatter(x_points, y_points, s=2, c='red')
plt.plot(x_points, [func(x, a, b, c) for x in x_points], c='green')
plt.title(f'Приблизні значення коефіцієнтів:\na={round(a, 4)}, b={round(b, 4)}, c={round(c, 4)}.')
plt.grid(True)
plt.show()

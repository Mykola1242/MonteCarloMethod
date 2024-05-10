import math
import random

import numpy as np
import matplotlib.pyplot as plt


def Func(x):
    y = np.sin(x) + np.cos(x) + 2
    return y


def MonteCarlo(N, S):
    K = 0
    for i in range(0, N):
        _x = random.uniform(0, 1)
        _y = random.uniform(0, 3.414)
        if _y < Func(_x):
            K += 1

    return S * (K / N)


x = np.linspace(0, 1, 100)

y = Func(x)

x_horizontal = [0, 1]
y_horizontal = [3.41421, 3.41421]

x_vertical_r = [1, 1]
y_vertical_r = [0, 3.41421]
x_vertical_l = [0, 0]
y_vertical_l = [0, 3.41421]

# y = []
#
# for val in x:
#     y.append(Func(val))

points = 100

print("Кількість згенерованих точок: ", points)
print("Площа криволінійної трапеції: ", MonteCarlo(points, 3.41421))

plt.fill_between(x, y, color='skyblue', alpha=0.5)
plt.plot(x, y, label='sin(x) + cos(x) + 2')
plt.title("Графік функції")
plt.xlabel("x")
plt.ylabel("y")
# plt.xlim(0, 1)  # Встановлення меж для вісі x
# plt.ylim(3, 3.5)  # Встановлення меж для вісі y

plt.axhline(0, color='black', linewidth=1, linestyle="--")
plt.axvline(0, color='black', linewidth=1, linestyle="--")
plt.grid(True)
plt.plot(x_horizontal, y_horizontal, color = "r")
plt.plot(x_vertical_r, y_vertical_r, color = "r")

plt.legend()

plt.show()

times = 10 #Кількість випробувань (10 разів)

amount_of_points = input("Уведіть кількість точок n, які будуть згенеровані для обчислення площі: ")

areas = []

for i in range(0, times):
    areas.append(MonteCarlo(int(amount_of_points), 3.41421))

print("Множина площ криволінійної трапеції: ", areas)

mathematical_expectation = sum(areas) / len(areas)

print("Математичне очікування M(S): ", mathematical_expectation)

# print("Different result")
# resi = 0
# for i in numb1:
#     resi += i
#
# resi = resi/len(numb1)
#
# print(resi)

# summary = 0
#
# for i in areas:
#     diff_squad = (i - mathematical_expectation) ** 2
#
#     summary += diff_squad
#
# desp = summary/len(areas)
#
# print(desp)

# print("Something different")

areas_for_desp = np.array(areas)
dif_sq = (areas_for_desp - mathematical_expectation) ** 2

dispersion = np.sum(dif_sq) / len(areas)
print("Дисперсія D: ", dispersion)



sqrt_disp = np.sqrt(dispersion)

print("Cередньоквадратичне відхилення √D: ", sqrt_disp)


print("Межі значення інтегралу (M(S) - σ) - (M(S) + σ): ", mathematical_expectation-sqrt_disp, " - ", mathematical_expectation+sqrt_disp)

area_integral = 3.30117

print("Абсолютна похибка Q=M(S)-S(T): ", mathematical_expectation-area_integral)

print(len(areas))


x_ = [100, 1000, 10000]
y_ = [0.063, 0.028, 0.004]

x_log = np.log10(x_)
y_log = np.log10(y_)

print(x_log)
print(y_log)

plt.plot(x_log, y_log, label='σ(n)')
plt.title("Графік залежності σ від n")
plt.xlabel("N")
plt.ylabel("σ")
plt.legend()
plt.xlim(0, 5)  # Встановлення меж для вісі x
plt.ylim(-4, 1)  # Встановлення меж для вісі y

plt.axhline(0, color='black', linewidth=1, linestyle="--")
plt.axvline(0, color='black', linewidth=1, linestyle="--")
plt.grid(True)




plt.show()

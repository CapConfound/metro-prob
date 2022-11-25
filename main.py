import scipy.stats
import numpy as np
import matplotlib.pyplot as plt

row = [385, 406, 388, 400, 408, 392, 413, 397, 392, 404, 386, 393, 368, 385, 405, 395, 390, 405, 405, 407, 386, 417, 410, 400, 388, 405, 380, 420, 402, 377]

prob_dover = 0.9545
z = 2

def elim_misses(row):
    print("Ряд элеметов: \n{}".format(row))
    # Определить объем ряда элементов:
    global n # Правильно
    n = len(row)
    print("Объем ряда элементов: {}".format(n))

    # Математическое ожидание:
    global expectedValue
    expectedValue = round((sum(row)/n), 2);
    print("Математическое ожидание: {}".format(expectedValue))

    # Абсолютная погрешность результатов наблюдения
    error_abs = []
    for x in row:
        error_abs.append(round((x - expectedValue), 2))

    print("Абсолютная погрешность результатов наблюдения:\n{}".format(error_abs))

    # Среднеквадратическое значение(СКО) многократного измерения

    sum1 = 0
    for x in error_abs:
        sum1 += pow(x, 2)

    global sko
    sko = round(pow((sum1 / (n - 1)), 0.5), 2)
    print("Среднеквадратическое значение(СКО) многократного измерения:\n{}".format(sko))


    # Поиск и исключение промахов.
    print("Была длина - {}".format(len(row)))

    i = 0;
    for x in error_abs:
        # print ("x = {} z * sko = {}".format(x, z*sko))
        if (abs(x) >= z * sko):
            print ("Удалил: {}. x = {} >= z * sko - {}".format(row[i], x, z * sko))
            row.pop(i)
            error_abs.pop(i)
        i += 1


    print("Стала длина - {}".format(len(row)))

    n = len(row)
    return row

i = 1
print("Этап {}".format(i))
prev_len = len(row)
row_mod = elim_misses(row)

print("prev_len - {}".format(prev_len))
print("len(row_mod) - {}".format(len(row_mod)))

while (len(row_mod) < prev_len):
    i += 1
    print("Этап {}".format(i))
    prev_len = len(row_mod)
    row_mod = elim_misses(row_mod)

print("row_mod final len - {}".format(len(row_mod)))
print("row final - {}".format(row_mod))

row_mod.sort()
rowF = row_mod
print ("row sorted (вариационный ряд)" + str(rowF))

x_min = min(rowF)
x_max = max(rowF)

print("min - {}".format(x_min))
print("max - {}".format(x_max))

print("Число эл-тов = {}\nОжидание = {}\nСКО = {}\n".format(n, expectedValue, sko))

# Чсло равных интервалов - бинов
r = 9

# Ширина бинов

r_width = (x_max - x_min) / r

print("Ширина бинов - {}".format(round(r_width, 3)))

bin_borders = []
mult = 0

z = x_min + (mult * r_width)

while (z <= x_max):
    bin_borders.append(round(z))
    mult += 1
    z = x_min + (mult * r_width)

print("Границы бинов: {}".format(bin_borders))


# Task 22

lowBord = x_min
sortedRow = rowF

histogram = plt.hist(sortedRow, bins = bin_borders, edgecolor = "black")

freqs = histogram[0]

print("Частоты попадания рез-тов наблюдений: {}".format(freqs))

control_n = 0
for i in freqs:
    control_n += i;

print("Значений - {}".format(control_n))


hit_probability = []
for i in freqs:
    prob = i / control_n
    hit_probability.append(round(prob, 4))

print("попадания значений вариационного ряда в каждый из бинов: {}".format(hit_probability))

avg_prob_dipersion_density = []
for i in hit_probability:
    item = i/r_width
    avg_prob_dipersion_density.append(round(item, 4))

print("Оценки средней плотности распределения вероятности в интервале : {}".format(avg_prob_dipersion_density))


skr_otkl = expectedValue / pow(control_n, 0.5)
print("Cреднеквадратическое отклонение среднеарифметических значений: {}".format(skr_otkl))

# Вычисление ширины доверительного интервала
stud = 1.699
dov_inter = stud * skr_otkl
print("Вычисление ширины доверительного интервала: {}".format(dov_inter))

# Результат измерения
print("result = {} ± {}".format(expectedValue, prob_dover))

plt.show()

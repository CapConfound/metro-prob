from math import floor, ceil, log, e, sqrt, pi, exp
import matplotlib.pyplot as pl
import seaborn as sns
import numpy as np

def midbin(k: int, xs: list) -> list:
    bins = []
    b = (max(xs) - min(xs)) / k
    xm = min(xs)

    for i in range(1, k + 1, 1):
        xci = xm + b * (i - 0.5)
        if xci > max(xs):
            break
        bins.append(xci)

    return bins


def intervals(k, xs) -> list:
    res = []
    b = (max(xs) - min(xs)) / k
    mids = midbin(k, xs)
    leftb = min(xs)
    rightb = leftb + b
    res.append([leftb, mids[0], rightb])
    for i in range(1, k, 1):
        leftb = rightb
        rightb = leftb + b
        res.append([leftb, mids[i], rightb])
    return res

def list_slice(array: list, start, fin) -> list:
    int = []
    for el in array:
        if el < start or el > fin:
            continue
        int.append(el)
    return int

def freq(array: list, start, fin, relative = False, cumulative = False) -> list:

    int = []
    for el in array:
        if el < start or el > fin:
            continue
        int.append(el)

    print('def freq - Ints:')
    print(int)

    if cumulative:
        ni = sum(int)
    else:
        ni = len(int)

    if relative:
        result = ni / len(array)
    else:
        result = ni

    return [int, result]


x = [
    24.44, 18.72, 41.16, 15.22, 6.64, 9.38, 52.47, 64.75, 40.11, 10.69, 40.24,
    53.65, 95.55, 48.30, 47.48, 88.33, 31.89, 17.10, 44.26, 51.47, 11.00, 98.17,
    17.58, 72.27, 64.27, 6.89, 86.58, 92.21, 9.15, 47.77, 77.41, 18.70, 53.89,
    51.88, 37.75, 68.27, 98.33, 52.48, 76.13, 25.13, 40.29, 51.64, 24.84, 63.00,
    90.93, 34.32, 68.75, 58.92, 52.53, 95.99
]
# x = [2.2, 18.43, 7.7, 19, 57.45, 88.86, 95.4, 86.28, 34.03, 52.51, 25.21, 27.26, 82.59, 7.72, 61.2, 51.64, 45.15, 54.7, 53.59, 96.54, 88.93, 32.83, 90.15, 66.38, 11.61, 73.79, 3.45, 30.25, 0.19, 45.83, 69.07, 17.21, 33.58, 65.12, 25.46, 23.11, 58.55, 69.29, 72.04, 51.69, 69.48, 7.3, 93.05, 45.36, 4.13, 13.69, 57.41, 51.25, 56.42, 19.84]
minX: float = min(x)
maxX: float = max(x)
xSort: list = sorted(x)
n: int = len(x)

print("Вариационный ряд:\n{}\n".format(xSort))

# Количество k интервалов разбиения диапазона
bin_num = floor(5 * log(n, 10))
print("Количество интервалов разбиения диапазона\n{}\n".format(bin_num))

b = (max(xSort) - min(xSort)) / bin_num

# bin_middle_list = list(midbin(bin_num, xSort))
ints = intervals(bin_num, xSort)
print("Разбил диапазон\n{}\n".format(ints))


# Найти для каждого интервала абсолютные и относительные частоты + абсолютные и относительные накопленные частоты
bin_contents = []
print("\nАбсолютная частота")
absol_f = []
for i in range(len(ints)):
    print("Для интервала ", i+1)
    [abs_inters, freq1] = freq(xSort, ints[i][0], ints[i][2])
    absol_f.append(freq1)
    print(freq1)
    bin_contents.append(abs_inters)

rel_f = []
print("\nОтносительная частота")
for i in range(len(ints)):
    print("Для интервала ", i+1)
    [rel_inters, freq2] = freq(xSort, ints[i][0], ints[i][2], True)
    rel_f.append(freq2)
    print(freq2)



print("\nАбсолютная накопленная частота")
abs_cum_freq = sum(absol_f)
print(abs_cum_freq)

print("\nОтносительная накопленная частота")
rel_cum_freq = abs_cum_freq / len(xSort)
print(rel_cum_freq)

# Выборочное среднее - относительные частоты * средние значения

vib_sr: float = 0
for i in range(len(ints)):
    vib_sr += rel_f[i] * ints[i][1]

sko: float = 0
for i in range(len(ints)):
    sko += pow((ints[i][1] - vib_sr), 2) * rel_f[i]
sko = sqrt(sko)


print("Абсолютная частота для нормального рпиблежения")
abs_freq_norm = []
for i in range(len(ints)):
    print("Для интервала ", i)
    temp = (1 / sqrt(2 * pi)) * exp(-0.5 * pow(((absol_f[i] - vib_sr) / sko) , 2))
    abs_freq_norm.append(temp)
    print(temp)

e = (1 / bin_num )


print(bin_contents) # Разбитые по бинам элементы

# Эмпирическая функция распределения - правильная
# sns.ecdfplot(xSort)
pl.hist(xSort, bins=bin_num, cumulative=True, density=1, edgecolor = 'black')
pl.title('Эмпирическая функция распределения')
dum = np.array(ints)
mids = dum[:, 1]
pl.xticks(mids)
pl.show()


# Гистограмма относительных частот
def plot_prep(item):
    return item/b

pl.figure(figsize=(20,6))
rel_f1 = list(map(plot_prep, rel_f))
pl.bar(mids, rel_f1, width=b, edgecolor='black')
pl.title('Гистограмма относительных частот')


# Доп. точки
x = [vib_sr]
for i in range(1, 4 ,1):
    x.append(vib_sr + (i * sko))
    x.append(vib_sr - (i * sko))
x.append(min(xSort))
x.append(max(xSort))
y = []
for i in range(len(x)):
    y.append(0)

pl.scatter(x, y, c=x, cmap='hot')

temp_mids = list(mids)
temp_mids.extend(x)
temp_mids = sorted(temp_mids)

pl.xticks(temp_mids)
pl.show()


# Полигон абсолютных частот
absciss = []
absciss.append(min(xSort))
absciss.extend(mids)
absciss.append(max(xSort))
print(absciss)

ordinate = []
ordinate.append(0)
ordinate.extend(absol_f)
ordinate.append(0)

ordinate1 = []
ordinate1.append(0)
ordinate1.extend(abs_freq_norm)
ordinate1.append(0)

pl.figure(figsize=(10,6))
pl.plot(absciss, ordinate)
pl.plot(absciss, ordinate1)
pl.title('Полигон абсолютных частот')

pl.xticks(absciss)
pl.ylim(0, 11)
pl.figure(dpi=280)
pl.show()


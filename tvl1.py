from math import floor, log, e, sqrt, pi, exp


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


def freq(array: list, start, fin, relative = False, cumulative = False) -> float:

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

    return result

def freq_norm(array: list, start, mid, fin):
    int = []
    for el in array:
        if el < start or el > fin:
            continue
        int.append(el)

    for i in range()
    x_d = freq(array, start, fin, True) * mid

    res = (1 / sqrt(2 * pi)) * exp(-0.5 * pow(((mid - x_d) / sx) , 2))



x = [
    24.44, 18.72, 41.16, 15.22, 6.64, 9.38, 52.47, 64.75, 40.11, 10.69, 40.24,
    53.65, 95.55, 48.30, 47.48, 88.33, 31.89, 17.10, 44.26, 51.47, 11.00, 98.17,
    17.58, 72.27, 64.27, 6.89, 86.58, 92.21, 9.15, 47.77, 77.41, 18.70, 53.89,
    51.88, 37.75, 68.27, 98.33, 52.48, 76.13, 25.13, 40.29, 51.64, 24.84, 63.00,
    90.93, 34.32, 68.75, 58.92, 52.53, 95.99
]
minX: float = min(x)
maxX: float = max(x)
xSort: list = sorted(x)
n: int = len(x)

print("Вариационный ряд:\n{}\n".format(xSort))

# Количество k интервалов разбиения диапазона
bin_num = floor(log(n, e))
print("Количество интервалов разбиения диапазона\n{}\n".format(bin_num))

#
# bin_middle_list = list(midbin(bin_num, xSort))
ints = intervals(bin_num, xSort)
print("Разбил диапазон\n{}\n".format(ints))


# Найти для каждого интервала абсолютные и относительные частоты + абсолютные и относительные накопленные частоты

print("\nАбсолютная частота")
absol_f = []
for i in range(len(ints)):
    print("Для интервала ", i+1)
    freq1 = freq(xSort, ints[i][0], ints[i][2])
    absol_f.append(freq1)
    print(freq1)

rel_f = []
print("\nОтносительная частота")
for i in range(len(ints)):
    print("Для интервала ", i+1)
    freq1 = freq(xSort, ints[i][0], ints[i][2], True)
    rel_f.append(freq1)
    print(freq1)


print("\nАбсолютная накопленная частота")
abs_cum_freq = sum(absol_f)
print(abs_cum_freq)

print("\nОтносительная накопленная частота")
rel_cum_freq = abs_cum_freq / len(xSort)
print(rel_cum_freq)

# Выборочное среднее - относительные частоты * средние значения




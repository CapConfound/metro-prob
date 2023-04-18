import math


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
    res.append({{'left', leftb}, {'mid', mids[0]}, {'right', rightb}})
    for i in range(1, k, 1):
        leftb = rightb
        rightb = leftb + b
        res.append({{'left', leftb}, {'mid', mids[i]}, {'right', rightb}})
    return res

def introw(xs: list, inters: list) -> list:
    i = 0
    res = {}
    for bin in inters:
        print(type(bin))
        # for x in xs:

            # if x > bin[2]:
            #     break
            # res[i] += x
            # i += 1
    return res
x = [
    24.44, 18.72, 41.16, 15.22, 6.64, 9.38, 52.47, 64.75, 40.11, 10.69, 40.24,
    53.65, 95.55, 48.30, 47.48, 88.33, 31.89, 17.10, 44.26, 51.47, 11.00, 98.17,
    17.58, 72.27, 64.27, 6.89, 86.58, 92.21, 9.15, 47.77, 77.41, 18.70, 53.89,
    51.88, 37.75, 68.27, 98.33, 52.48, 76.13, 25.13, 40.29, 51.64, 24.84, 63.00,
    90.93, 34.32, 68.75, 58.92, 52.53, 95.99
]
minX:   float = min(x)
maxX:   float = max(x)
xSort:  list = sorted(x)
n:      int = len(x)

print("Вариационный ряд:\n{}\n".format(xSort))

# Количество k интервалов разбиения диапазона
bin_num = math.floor(math.log(n, math.e))
print("Количество интервалов разбиения диапазона\n{}\n".format(bin_num))

#
# bin_middle_list = list(midbin(bin_num, xSort))
ints = intervals(bin_num, xSort)
print("Разбил диапазон\n{}\n".format(intervals))

introv = introw(xSort, ints)
print(introv)

# Найти для каждого интервала абсолютные и относительные частоты + абсолютные и относительные накопленные частоты
absolute = []

# for i in range(bin_num):



print("Абсолютная накопленная частота")

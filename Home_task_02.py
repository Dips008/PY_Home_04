# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

n = int(input('Enter the number N = '))


def multipliers(e):
    i = 2
    mult = []
    while e > 1:
        if e % i == 0:
            mult.append(i)
            e = e / i
        else:
            i += 1
    return mult


print(multipliers(n))

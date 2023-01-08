# Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен
# степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

k = int(input('Enter the natural degree k = '))
coeff = [random.randint(0, 101) for i in range(k+1)]
print(k, ' => ', coeff)


def str_polite_file(st):
    with open('Home_task_04.txt', 'w') as data:
        data.write(st)


def get_polynomial(k, coeff):
    str_pol = ''
    if k+1 <= 1:
        str_pol = 'x = 0'
    else:
        for i in range(k+1):
            if i != k+1 - 1 and k+1 != 0 and i != k+1 - 2:
                str_pol += f'{coeff[i]}*x^{k+1 - i - 1}'
                if list[i + 1] != 0:
                    str_pol += ' + '
            elif i == k+1 - 2 and k+1 != 0:
                str_pol += f'{coeff[i]}*x'
                if list[i + 1] != 0:
                    str_pol += ' + '
            elif i == k+1 - 1 and k+1 != 0:
                str_pol += f'{coeff[i]} = 0'
            elif i == k+1 - 1 and k+1 == 0:
                str_pol += ' = 0'
    return str_pol


print(get_polynomial(k, coeff))

str_polite_file(get_polynomial(k, coeff))

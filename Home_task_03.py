# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
import random

res = [random.randint(0, 5) for i in range(10)]
print(res)

res = set(res)
print(res)

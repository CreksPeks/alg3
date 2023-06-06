

from random import randint

n = 10                                               # длинна списка
lst = [randint(0, 99) for i in range(n)]             # рандомный список
x = 1                                                # счетчик проходов
for i in range(n):
    for j in range(n - 1 - i):                       # добавляем "-i" что бы не проходить каждый раз по всему списку, т.к. с каждым проходом одно число встает на место
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
    if lst[0] == min(lst) or lst[0] == max(lst):     # в зависимости от того в какую сторону сортируем, выполняется одна или другая проверка
        break
    x += 1
print(x)                                             # кол-во проходов
print(lst)                                           # результат
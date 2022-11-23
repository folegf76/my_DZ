# 1  Реалізуйте генераторну функцію, яка повертатиме по одному члену числової послідовності, закон якої задається за
# допомогою функції користувача. Крім цього параметром генераторної функції повинні бути значення першого члена
# прогресії та кількість членів, що видаються послідовностю. Генератор повинен зупинити свою роботу або по досягненню
# n-го члена, або при передачі команди на завершення.

def generator(start, n, funcs):
    while n > 0:
        yield start
        start = funcs(start)
        n = n - 1


g = generator(1, 10, lambda x: x * 2)

for i in g:
    if i > 100:
        g.close()
    print(i)

# 2 Використовуючи замикання, реалізуйте такий прийом програмування як Мемоізація -
# https://en.wikipedia.org/wiki/Memoization . Використовуйте отриманий механізм для прискорення функції рекурсивного
# обчислення n - го члена ряду Фібоначчі. Порівняйте швидкість виконання із просто рекурсивним підходом.

import timeit

s1 = '''
def fibo(n):
    if n < 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


print(fibo(20))
'''

s2 = '''
def fibo_2():
    memo = [1, 1]

    def number(n):
        if n < len(memo):
            return memo[n]
        else:
            memo.append(number(n - 1) + number(n - 2))
        return memo[-1]
    return number


f = fibo_2()
print(f(20))
# '''

print(timeit.timeit(s1, number=10))
print(timeit.timeit(s2, number=10))

# 3 Напишіть функцію, яка застосує до списку чисел довільну функцію користувача і поверне суми елементів отриманого
# списку.

def my_summ(a, f):
    temp = []
    for i in a:
        temp.append(f(i))
    return sum(temp)


a = [2, 3, 50, 6, 8, 10]
print(my_summ(a, lambda x: x ** 2))

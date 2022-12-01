# 1 Создайте декоратор, который будет подсчитывать, сколько раз была вызвана декорируемая функция.

class Decor:

    def __init__(self, func):
        self.func = func
        self.quan = 0

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        self.quan += 1
        return result


@Decor
def summa_1(a, b):
    return a + b


@Decor
def summa_2(a, b, c):
    return a + b + c


print(summa_1(5, 3))
print(summa_1(5, 3))
print(summa_1(5, 3))
print(summa_2(1, 2, 3))
print(summa_1.quan)
print(summa_2.quan)


# 2 Создайте декоратор, который зарегистрирует декорируемую функцию в списке функций, для обработки последовательности.

list_f = []


def decor(f):
    if f not in list_f:
        list_f.append(f)
    return f


@decor
def test(x, y):
    return x + y


@decor
def test_2(x, y, z):
    return x + y + z


print(test(1, 5))
print(test(2, 5))
print(test_2(3, 5, 3))

print(list_f)

# 3 Предположим, в классе определен метод __str__, который возвращает строку на основании класса. Создайте такой
# декоратор для этого метода, чтобы полученная строка сохранялась в текстовый файл, имя которого совпадает с именем
# класса, метод которого вы декорировали.

def decor(f):
    def f_decor(data):
        file = open(f'{data.__class__.__name__}.txt', "w")
        temp = f(data)
        file.write(temp)
        file.flush()
        file.close()
        return temp
    return f_decor


class Cat:

    def __init__(self, name):
        self.name = name

    @decor
    def __str__(self):
        return f"{self.name}"


c = Cat("Murca")
print(c)

# 4 Создайте декоратор с параметрами для проведения хронометража работы той или иной функции. Параметрами должны
# выступать то, сколько раз нужно запустить декорируемую функцию и в какой файл сохранить результаты хронометража.
# Цель - провести хронометраж декорируемой функции

import time


def parameter(number=10, file_name="test.txt"):
    def decorator(f):
        def decor(*args):
            i = 0
            start = time.time()
            while i < number:
                res = f(*args)
                i += 1
            stop = time.time()
            file = open(file_name, "w")
            file.write(f"Start {start}, stop {stop} = {stop - start} sec")
            file.close()
            return res
        return decor
    return decorator


@parameter(number=1000)
def func_test():
    resau = 0
    for i in range(10000):
        resau += 1
    return resau


print(func_test())

# 5.1 Создайте декоратор, который зарегистрирует декорируемый класс в списке классов

list_class = []


def decor(cls):
    if cls not in list_class:
        list_class.append(cls)
    return cls


@decor
class Cat:

    def __init__(self, name):
        self.name = name

print(list_class)

# 5.2 Создайте декоратор класса с параметром. Параметром должна быть строка, которая должна дописываться (слева) к
# результату работы метода __str__.


def add_list(text):
    def decorator(cls):
        def decor(*args, **kwargs):
            ob_cl = cls(*args, **kwargs)
            return text + ob_cl.__str__()
        return decor
    return decorator


@add_list("Hello ")
class Cat:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"


cat1 = Cat("Murka")
cat2 = Cat("Tom")
print(cat1)
print(cat1)
print(cat2)

# 5.3 Для класса Box напишите статический метод, который будет подсчитывать суммарный объем двух ящиков, которые будут
# его параметрами

class Box:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f"{self.a}, {self.b}, {self.c}"

    def volume(self):
        return self.a * self.b * self.c

    @staticmethod
    def volume_2(box_1, box_2):
        return box_1.volume() + box_2.volume()


box_1 = Box(1, 1, 1)
box_2 = Box(2, 2, 2)
print(Box.volume_2(box_1, box_2))
print(box_1.volume_2(box_1, box_2))



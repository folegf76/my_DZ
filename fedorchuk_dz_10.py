# 1) Создайте дескриптор, который будет делать поля класса управляемые им доступными только для чтения.

class MyDescriptor:

    def __init__(self):
        pass

    def __get__(self, instance_self, instance_class):
        return instance_self.p

    def __set__(self, instance_self, value):
        raise AttributeError("field is read only")

    def __delete__(self, instance_self):
        raise AttributeError("cannot delete field")


class Box:
    def __init__(self, x, y, z):
        self.p = x*y*z

    volume = MyDescriptor()


box_1 = Box(1, 2, 3)
print(box_1.volume)

# 2) Реализуйте функционал, который будет запрещать установку полей класса любыми значениями, кроме целых чисел. Т.е.,
# если тому или иному полю попытаться присвоить, например, строку, то должно быть возбужденно исключение.

class Box:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f"Box: a = {self.a}, b = {self.b}, c = {self.c}"

    def __setattr__(self, attr_name, attr_value):
        if isinstance(attr_value, int):
            self.__dict__[attr_name] = attr_value
        else:
            raise TypeError


box_1 = Box(1, 2, 3)
print(box_1)
box_1.a = 5
print(box_1)

# 3) Реализуйте свойство класса, которое обладает следующим функционалом: при установки значения этого свойства в файл
# с заранее определенным названием должно сохранятся время (когда устанавливали значение свойства) и установленное
# значение.

import datetime


class Cat:

    def __init__(self, __name, age):
        self.__name = __name
        self.age = age

    name = property()

    @name.getter
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_value):
        self.__name = name_value
        file = open('Test.txt', "w")
        file.write(str(datetime.datetime.now()) + " - ")
        file.write(str(name_value) + '\n')
        file.close()

    def __str__(self):
        return f"Name - {self.__name}, age - {self.age}"


cat_1 = Cat("Murka", 5)
cat_1.name = "Tom"
print(cat_1)
print(cat_1.name)

# 4) 1) Создайте ABC класс с абстрактным методом проверки целого числа на простоту. Т.е., если параметром этого метода
# является целое число и оно простое, то метод должен вернуть True, а в противном случае False.
# 2) Создайте класс его наследующий.
# 3) Создайте класс, который не наследует пользовательский ABC класс, но обладает нужным методом. Зарегистрируйте его
# в качестве виртуального подкласса.
# 4) Проверьте работоспособность проекта

import abc


class AbstractValidator(abc.ABC):

    @abc.abstractmethod
    def validate(self, number):
        if isinstance(number, int):
            for i in range(2, abs(number) // 2 + 1):
                if number % i == 0:
                    return False
        else:
            return False
        return True


class Heir(AbstractValidator):

    def validate(self, number):
        return number


class Virtual:

    def validate(self, number):
        if isinstance(number, int):
            for i in range(2, abs(number) // 2 + 1):
                if number % i == 0:
                    return False
        else:
            return False
        return True


AbstractValidator.register(Virtual)

heir = Heir()
virtual = Virtual()
print(isinstance(heir, AbstractValidator))
print(isinstance(virtual, AbstractValidator))
print(virtual.validate(19))


class Product:

    def __init__(self, title: str, price: float | int):
        self.title = title
        self.price = price

    def __str__(self):
        return f'{self.title}: {self.price}'


class Customer:

    def __init__(self, surname: str, name: str):
        self.surname = surname
        self.name = name

    def __str__(self):
        return f'{self.surname} {self.name[0]}.'


class OrderIterator:

    def __init__(self, order_list, quantities_list):
        self.order_list = order_list
        self.quantities_list = quantities_list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.order_list):
            raise StopIteration
        temp_order = (self.order_list[self.index], self.quantities_list[self.index])
        self.index += 1
        return temp_order


class Order:

    def __init__(self, customer: Customer):
        self.customer = customer
        self.__products = []
        self.__quantities = []

    def add_product(self, product: Product, quantity=1):
        self.__products.append(product)
        self.__quantities.append(quantity)

    def total(self):
        summa = 0
        for index, product in enumerate(self.__products):
            summa += product.price * self.__quantities[index]
        return summa

    def __str__(self):
        res = ''
        for product, quantity in zip(self.__products, self.__quantities):
            res += f'{product} x {quantity} = {product.price * quantity} грн.\n'
        return f'{self.customer}\n' \
               f'{res}\n' \
               f'Total={self.total()} грн.'

    def __getitem__(self, item):
        if isinstance(item, int):
            if 0 <= item < len(self.__products):
                return self.__products[item]
            else:
                raise IndexError()
        if isinstance(item, slice):
            start = item.start or 0
            stop = item.stop or len(self.__products)
            step = item.step or 1
            temp_list = []
            if start < 0 and stop >= len(self.__products):
                raise IndexError()
            for i in range(start, stop, step):
                temp_list.append(self.__products[i])
            return temp_list
        raise TypeError()

    def __len__(self):
        return len(self.__products)

    def __iter__(self):
        return OrderIterator(self.__products, self.__quantities)


pr_1 = Product('apple', 20)
pr_2 = Product('orange', 21)
pr_3 = Product('banana', 23)
pr_4 = Product('apple2', 30)
pr_5 = Product('apple3', 40)
pr_6 = Product('apple4', 50)

customer_1 = Customer('Ivanov', 'Ivan')

order_1 = Order(customer_1)
order_1.add_product(pr_1)
order_1.add_product(pr_2, 20)
order_1.add_product(pr_3, 30)
order_1.add_product(pr_4, 40)
order_1.add_product(pr_5, 50)
order_1.add_product(pr_6, 60)


for i, j in order_1:
    print(i, j)
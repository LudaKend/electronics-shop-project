# класс Item содержит атрибуты:
#- название товара: name
#- цена за единицу товара: price
#- количество товара в магазине: quantity

#импортирую модуль csv, позволяющий работать с текстовым файлом с разделителями, у которого расширение .csv
import csv


class Item:
    pay_rate = 1
    all = []
    def __init__(self, name, price, quantity):
        self.__name = name
        self.price = price
        self.quantity = quantity
#        self.discount_price = price * pay_rate
# добавление новых экземпляров (из прошлого Д/З закомментируем, потому что экземпляры будем создавать из csv-файла
#        Item.all.append(self)


    def __repr__(self):
        return f"Item({self.__name},{self.price}, {self.quantity})"

    def calculate_total_price(self):
        '''получает общую стоимость конкретного товара в магазине'''
        return self.price * self.quantity

    def apply_discount(self):
        '''применяет установленную скидку для конкретного товара'''
        self.price = self.price * self.pay_rate   #такой синтаксис для конкретного экземпляра!
        return self.price


    @property
    def name(self):
        '''создаю сеттер для приватного атрибута __name с помощью декоратора property'''
        return self.__name

    @name.setter
    def name(self, name):
        '''прописываю геттер для приватного атрибута __name с помощью декоратора property, сразу обрезаю'''
        self.__name = name[:10]


    @classmethod
    def instantiate_from_csv(cls):
        ''' класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv'''
        cls.all.clear()
 #       print(Item.all)         # для отладки
        with open('../src/items.csv') as f:
            data_file = csv.DictReader(f)
            for line in data_file:
                item1 = (cls(line['name'], line['price'], line['quantity']))
 #               print(item1)  # для отладки
                cls.all.append(item1)
 #           print(len(Item.all))  # для отладки

    @staticmethod
    def string_to_number(item_string):
        number = float(item_string)
        return int(number)


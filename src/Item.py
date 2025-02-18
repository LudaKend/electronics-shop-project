# класс Item содержит атрибуты:
#- название товара: name
#- цена за единицу товара: price
#- количество товара в магазине: quantity

#импортирую модуль csv, позволяющий работать с текстовым файлом с разделителями, у которого расширение .csv
import csv
import os


class InstantiateCSVError(Exception):
    '''собственный класс-исключение для проверки файла на повреждение'''
    def __init__(self, *args, **kwargs):
        self.message = '_Файл items.csv поврежден_' #args[0] if args else '_Файл items.csv поврежден_'

    def __str__(self):
        return self.message

class CantOpen(Exception):
    '''собственный класс-исключение для проверки успешности открытия файла'''
    def __init__(self, *args, **kwargs):
        self.message = 'Файл не открывается'

    def __str__(self):
        return self.message

class Item:
    pay_rate = 1
    all = []
    def __init__(self, name, price, quantity):
        self.__name = name
        self.price = price
#        print(quantity)
        self.quantity = int(quantity)
#        self.discount_price = price * pay_rate
# добавление новых экземпляров (из прошлого Д/З закомментируем, потому что экземпляры будем создавать из csv-файла
#        Item.all.append(self)

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
    def instantiate_from_csv(cls, filename='items.csv'):
        ''' класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv'''
        cls.all.clear()
 #       print(Item.all)         # для отладки
        if os.path.exists(f'../src/{filename}') == False:
            raise FileNotFoundError(f'Отсутствует файл {filename}')
        else:
            try:
                path = f'../src/{filename}'
                f = open(path, encoding='cp1251')
                data_file = csv.DictReader(f)
            except:
                raise CantOpen
            for line in data_file:

                if len(line['quantity']) == 0:
                    raise InstantiateCSVError

                item1 = (cls(line['name'], line['price'], line['quantity']))

                cls.all.append(item1)

        #finally:
            f.close()


    @staticmethod
    def string_to_number(item_string):
        number = float(item_string)
        return int(number)

    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if isinstance(self, Item) and isinstance(other, Item):
            return self.quantity + other.quantity
        return f'складывать можно только объекты класса Item и Phone'




# класс Phone наследует атрибуты из класса Item:
#- название товара: name
#- цена за единицу товара: price
#- количество товара в магазине: quantity

#содержит новый атрибут:
#- количество сим-карт: number_of_sim

from src.Item import Item

class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        super().__repr__()
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other):
        '''метод для сложения экземпляров только внутри класса Phone'''
        if isinstance(self, Phone) and isinstance(other, Phone):
            return self.quantity + other.quantity
        return f'складывать можно только объекты класса Phone'


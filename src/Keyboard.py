# класс Keyboard наследует атрибуты из класса Item:
#- название товара: name
#- цена за единицу товара: price
#- количество товара в магазине: quantity

#содержит новый атрибут:
#- язык: language

from src.Item import Item

class MixinLaung:
    '''миксин-класс для хранения и изменения раскладки клавиатуры'''
    def __init__(self, language):
        self.language = language

    def change_lang(self):
        '''метод для смены языка в раскладке клавиатуры'''
        if self.language == 'EN':
            self.language = 'RU'
        else:
            self.language = 'EN'

    def __str__(self):
        return f'{self.language}'

class Keyboard(Item, MixinLaung):
    def __init__(self, name, price, quantity, language='EN'):
        super().__init__(name, price, quantity)
        self.language = language

    def __repr__(self):
        return f"Keyboard('{self.name}', {self.price}, {self.quantity}, {self.language})"


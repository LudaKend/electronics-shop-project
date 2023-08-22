# класс Item содержит атрибуты:
#- название товара: name
#- цена за единицу товара: price
#- количество товара в магазине: quantity

class Item:
    pay_rate = 1
    all = []
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
#        self.discount_price = price * pay_rate

        Item.all.append(self)


    def __repr__(self):
        return f"Item({self.name},{self.price}, {self.quantity})"

    def calculate_total_price(self):
        '''получает общую стоимость конкретного товара в магазине'''
        return self.price * self.quantity

    def apply_discount(self):
        '''применяет установленную скидку для конкретного товара'''
        self.price = self.price * self.pay_rate   #такой синтаксис для конкретного экземпляра!
        return self.price



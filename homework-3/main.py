from src.Item import Item

if __name__ == '__main__':
    item1 = Item("Смартфон", 10000, 20)

    assert repr(item1) == "Item('Смартфон', 10000, 20)"
 #   print(item1.__repr__)
    assert str(item1) == 'Смартфон'
 #   print(item1)
 #   print(item1.name)

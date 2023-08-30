"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.Item import Item


@pytest.fixture
def item_test():
    return Item("Мышь", 1000, 1000)


def test_item_calculate_total_price(item_test):
    '''тестируем метод подсчета общей стоимости'''

    assert item_test.calculate_total_price() == 1000000

def test_item_apply_discount(item_test):
    '''тестируем применение скидки для конкретного товара'''

    assert item_test.apply_discount() == 1000

def test_instantiate_from_csv():
    assert len(Item.all) == 0

def test_string_to_number():
    '''тестируем преобразование строки в целое число'''

    assert Item.string_to_number('7.7') == 7

def test_repr(item_test):
    '''тестируем вывод атрибутов для отладки, используя фикстуру'''
    assert item_test.__repr__() == "Item('Мышь', 1000, 1000)"

def test_str(item_test):
    '''тестируем пользовательский вывод атрибутов класса, используя фикстуру'''
    assert item_test.__str__() == 'Мышь'


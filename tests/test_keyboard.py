"""Здесь надо написать тесты с использованием pytest для модуля Keyboard."""

import pytest
from src.Item import Item
from src.Keyboard import Keyboard

@pytest.fixture
def keyboard_test():
    return Keyboard("Клавиатура удобная", 300, 5550)

def test_repr(keyboard_test):
    '''тестируем вывод атрибутов для отладки, используя фикстуру'''
    assert keyboard_test.__repr__() == "Keyboard('Клавиатура удобная', 300, 5550, EN)"

def test_item_calculate_total_price(keyboard_test):
    '''тестируем метод подсчета общей стоимости'''

    assert keyboard_test.calculate_total_price() == 1665000

def test_item_apply_discount(keyboard_test):
    '''тестируем применение скидки для конкретного товара'''

    assert keyboard_test.apply_discount() == 300
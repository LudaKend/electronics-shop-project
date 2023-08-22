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

"""Здесь  тесты с использованием pytest для модуля phone."""

import pytest
from src.phone import Phone
from src.Item import Item

@pytest.fixture
def phone_test():
    return Phone("Super iPhone", 1000000, 1, 5)


def test_repr(phone_test):
    '''тестируем вывод атрибутов для отладки, используя фикстуру'''
    assert phone_test.__repr__() == "Phone('Super iPhone', 1000000, 1, 5)"

def test_str(phone_test):
    '''тестируем пользовательский вывод атрибутов класса, используя фикстуру'''
    assert phone_test.__str__() == 'Super iPhone'

def test_add(phone_test):
    '''тестируем метод сложения для атрибута quantity'''
    phone_test2 = Phone("Super Xiaomi", 950000, 2, 3)
    assert phone_test + phone_test2 == 3
    item_test2 = Item("HD-кабель", 1500, 770)
    assert phone_test + item_test2 == 'складывать можно только объекты класса Phone'

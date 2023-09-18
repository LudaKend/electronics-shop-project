from src.Keyboard import Keyboard

if __name__ == '__main__':
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"

    assert str(kb.language) == "EN"

    kb.change_lang()
    assert str(kb.language) == "RU"

    #print(kb.__dict__)
    #print(Keyboard.__mro__)

    # Сделали RU -> EN -> RU
    # kb.change_lang().change_lang()
    # assert str(kb.language) == "RU"
    kb.change_lang()
    assert str(kb.language) == "EN"

    kb.language = 'CH'
    # AttributeError: property 'language' of 'Keyboard' object has no setter

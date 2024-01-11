from classes.class_utils import Hangman


def test_wrong():
    """
    Тест экземпляра класса wrong класса Hangman
    """
    assert Hangman('abs', 'abs').wrong == 'abs'

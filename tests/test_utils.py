from utils.utils import *


def test_word_list():
    """
    Тест функции word_list которая на выходе получаем список
    """
    assert word_list([{'a': 'Hello'}]) == ["a", "Hello"]

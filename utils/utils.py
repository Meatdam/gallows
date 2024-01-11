import json
import random
from config import ROOT_DIR
import os

VISELICA_PATH = os.path.join(ROOT_DIR, 'utils', 'viselica.json')


def load_json_file():
    """
    Загружает и возвращяет json файл
    """
    with open(VISELICA_PATH) as file:
        content = json.load(file)
    return content


def word_list(values):
    """
    Из json файла рондомно забреает ключ и значение,
    преобразует словарь в список.
    """
    word_random = random.choice(values)
    list_word = []
    for k, v in word_random.items():
        list_word.append(k)
        list_word.append(v)
    return list_word

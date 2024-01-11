from utils.utils import *
from classes.class_utils import Hangman
import copy


result = Hangman(0)
content = word_list(load_json_file())
contents = ''.join(content[0])
contents_copy = list(copy.copy(contents))
boards = result.board * len(contents)
len_points = 0
list_points = []

print("\nДобро пожаловать на казнь!\n==========================")
print(f"Отгадаешь будешь жить:\n{''.join(content[1])}\n\nВ слове {len(contents)} символов")
print(f"\n{' '.join(boards)}\n")

while result.wrong < len(result.stages) - 1:
    if len(list_points) == len(contents):
        result.win = True
        break

    user_input = input("введите букву:\n").strip().lower()
    if len(user_input) == 0:
        result.wrong += 1
        print(boards)
        e = result.wrong + 1
        print("УПС...Такой буквы нет :(")
        print("\n".join(result.stages[0: e]))
        continue

    if user_input == ''.join(contents):
        result.win = True
        break

    if user_input in contents_copy:
        contents_copy.remove(user_input)
        len_points += 1
        list_points.append(contents)
        cind = contents.index(user_input)
        boards[cind] = user_input.upper()
        points = len(contents) - len_points
        print(f"Есть такая буква! Осталось угадать {points} букв\n")
        print(' '.join(boards))

    else:
        result.wrong += 1
        print(boards)
        e = result.wrong + 1
        print("УПС...Такой буквы нет :(")
        print("\n".join(result.stages[0: e]))

if not result.win:
    print(f"Вы проиграли! было загадано слово: {contents}.")

if result.win:
    print(f"Конечно же:\n{''.join(content[1])}\nэто {contents}")

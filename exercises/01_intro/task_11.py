"""
Запросити користувача введення кольору через input.

Якщо введений колір є у списку colors, вивести повідомлення "Такий колір є".
Якщо немає кольору, вивести повідомлення "У списку colors немає такого кольору".

Зробити так, щоб користувач міг вводити колір у будь-якому регістрі, але при
цьому перевірка для слова працювала (нижче приклад).

В завданні дві версії списку colors: простіший варіант і ускладнений.
Спочатку варто спробувати простіший варіант і переходити на ускладнений
тільки, якщо все вийде з першим варіантом і буде бажання.
colors = ["green", 'red', 'pink', 'yellow', 'white', 'black']
colors = ["Green", 'RED', 'Pink', 'YELLOW', 'white', 'Black']

Приклад роботи завдання
$ python task_11.py
Введіть колір: red
Такий колір є

$ python task_11.py
Введіть колір: Red
Такий колір є

$ python task_11.py
Введіть колір: RED
Такий колір є

$ python task_11.py
Введіть колір: blue
У списку colors немає такого кольору

При цьому не можна змінювати список colors.
"""
# Version 1
colors = ["green", 'red', 'pink', 'yellow', 'white', 'black']
ускладнена версія
colors_raw = ["Green", 'RED', 'Pink', 'YELLOW', 'white', 'Black']
colors = []
for col in colors_raw:
    colors.append(col.lower())

color = input("Введіть колір: ")

if color.lower() in colors:
    print("Такий колір є")
else:
    print("У списку colors немає такого кольору")

# Version 2
# colors = ["Green", 'RED', 'Pink', 'YELLOW', 'white', 'Black']
# user_color = input("Введіть колір: ")
#
# message = "У списку colors немає такого кольору"
# for color in colors:
#     if color.lower() == user_color.lower():
#         message = "Такий колір є"
#
# print(message)

# Version 3
# colors = ["Green", 'RED', 'Pink', 'YELLOW', 'white', 'Black']
# user_color = input("Введіть колір: ")
#
# found_color = False
# for color in colors:
#     if color.lower() == user_color.lower():
#         found_color = True
#
# # if found_color == True:
# if found_color:
#     print("Такий колір є")
# else:
#     print("У списку colors немає такого кольору")

"""
Якщо запустити код завдання, на екран буде виведено:
$ python task_01.py
Python is a high-level, interpreted, general-purpose programming language.

Необхідно змінити рядок start_data таким чином, щоб на екран було виведено
$ python task_01.py
Ruby is a high-level, interpreted, general-purpose programming language.

При цьому не можна змінювати рядок start_data вручну, тільки за допомогою Python.
"""
start_data = "Python is a high-level, interpreted, general-purpose programming language."
print(start_data)

# new_data = start_data.replace("Python", "Ruby")
# print(new_data)

part = start_data[6:]
result = "Ruby" + part
print(result)

# З нюансами роботи lstrip
# part = start_data.lstrip("Python")
# print("Ruby" + part)

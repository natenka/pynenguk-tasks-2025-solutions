"""
Якщо запустити код завдання, на екран буде виведено:
$ python task_02.py
Python is a high-level, interpreted, general-purpose programming language.

Необхідно змінити рядок start_data за допомогою Python таким чином, щоб на
екран було виведено такий рядок (видалити коми та крапку):
$ python task_02.py
Python is a high-level interpreted general-purpose programming language

При цьому не можна змінювати рядок start_data вручну, тільки за допомогою Python.
"""
start_data = "Python is a high-level, interpreted, general-purpose programming language."
print(start_data)

# new_data = start_data.replace(",", "")
# print(new_data[:-1])
#
# new_data = start_data.replace(",", "")[:-1]
# print(new_data)

# print(start_data.replace(",", "").replace(".", ""))
# new_data = start_data.replace(",", "").replace(".", "")
# print(new_data)


new_data = start_data.replace(",", "").rstrip(".")
print(new_data)

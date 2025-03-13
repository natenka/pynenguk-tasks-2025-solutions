"""
Запросити у користувача введення індексу (числа) через input. Якщо за введеним
індексом можна вивести слово зі списку words, вивести його. Якщо індекс більший
за допустимий, вивести повідомлення "У списку words немає такого індексу".


Приклад роботи завдання
$ python task_07.py
Введіть індекс: 0
word1

$ python task_07.py
Введіть індекс: 2
word3

$ python task_07.py
Введіть індекс: 5
У списку words немає такого індексу

Завдання можна ускладнити, додавши підтримку негативних індексів:

$ python task_07.py
Введіть індекс: -1
word3

$ python task_07.py
Введіть індекс: -3
word1

$ python task_07.py
Введіть індекс: -4
У списку words немає такого індексу
"""
words = ["word1", "word2", "word3"]

index_input = input("Введіть індекс: ")
index = int(index_input)

# if index == 0 or index == 1 or index == 2:
# if index in [0, 1, 2]:
# if index >= 0 and index < len(words):
# if -3 <= index < 3:

len_words = len(words)
if -len_words <= index < len_words:
    print(words[index])
else:
    print("У списку words немає такого індексу")

# 3 items: 0 1 2  -1 -2 -3
# 5 items: 0 1 2 3 4  -1 -2 -3 -4 -5

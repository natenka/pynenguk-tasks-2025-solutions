"""
Додайте рядок у змінній new_word у кінець списку слів.

Після оновлення списку вивести його на екран за допомогою print.

Список words не можна змінювати вручну, тобто не можна дописувати слово
"result" наприкінці списку, треба змінити його за допомогою Python.
"""

words = ["line", "test", "column"]
new_word = "result"
print(words)
words.append(new_word)
print(words)

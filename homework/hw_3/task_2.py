"""
В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых. 
Не учитывать знаки препинания и регистр символов.
Слова разделяются пробелами, апостроф не считается за пробел. 
Такие слова как dont, its, didnt итд (после того, как убрали знак препинания апостроф) считать одним словом.
"""

import re

# text = "Hello world. Hello Python. Hello again."
# text = "Python 3.9 is the latest version of Python. It's awesome!"
# text = 'Python is python, is, IS, and PYTHON.'
text = ("Python is an interpreted, high-level, general-purpose programming language. "
        "Created by Guido van Rossum and first released in 1991, Python's design philosophy "
        "emphasizes code readability with its notable use of significant whitespace. "
        "Its language constructs and object-oriented approach aim to help programmers write clear, "
        "logical code for small and large-scale projects.")

data = re.sub(r'[^\w\s]+|\d', '', text.lower()
              .replace('-', ' ').replace("'", ' '))
data = data.split(' ')

tmp = []
words_count = []
for w in data:
    if w not in tmp and w != '':
        tmp.append(w)
        words_count.append((w, data.count(w)))

for limit in range(len(words_count) - 1, 0, -1):
    for i in range(limit):
        if words_count[i][1] < words_count[i + 1][1]:
            words_count[i], words_count[i + 1] = words_count[i + 1], words_count[i]

print(words_count[:10])

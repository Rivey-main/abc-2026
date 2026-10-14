import os

path = os.path.join(os.path.dirname(__file__), 'inverted_sort.txt')

with open(path, 'r+', encoding='utf-8') as f:
    lines = f.readlines()
    f.writelines(lines[::-1])

max_num = lambda a, b: a if a > b else b

print(max_num(15, 42))


mass = [122, 23, 1425, 23, 768, 4, 67, 998, 4, 6, 867]

check_list = [1 <= val <= 130 for val in mass]

print(check_list)


list_ = [10, 11, 14, 25, 33, 36, 100, 101]

filtered_list = list(filter(lambda val: val % 2 != 0, list_))

print(filtered_list)


files = ['file.txt', 'file2.mp3', 'file.pdf', 'file3.mp3', '.mp3le.doc']

sorted_files = sorted(files, key=lambda f: not f.endswith('.mp3'))

print(sorted_files)

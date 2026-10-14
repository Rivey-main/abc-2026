f = open("text.txt", "w+t")
f.write("Hello\n")


f.seek(0)             # Возвращаем указатель в начало файла
content = f.read()    # Считываем записанное приветствие
print(content.strip()) # Выводим в консоль (убирая лишние переносы строк)

f.close()

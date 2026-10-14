# todo: Шифр Цезаря
Описание шифра.
В криптографии шифр Цезаря, также известный шифр сдвига, код Цезаря или сдвиг Цезаря,
является одним из самых простых и широко известных методов шифрования.
Это тип подстановочного шифра, в котором каждая буква в открытом тексте заменяется буквой на некоторое
фиксированное количество позиций вниз по алфавиту. Например, со сдвигом влево 3, D будет заменен на A,
E станет Б, и так далее. Метод назван в честь Юлия Цезаря, который использовал его в своей частной переписке.

Задача.
Считайте файл message.txt и зашифруйте  текст шифром Цезаря, при этом символы первой строки файла должны
циклически сдвигаться влево на 1, второй строки — на 2, третьей строки — на три и т.д.
В этой задаче удобно считывать файл построчно, шифруя каждую строку в отдельности.
В каждой строчке содержатся различные символы. Шифровать нужно только буквы кириллицы.


import string
FROM python:3.11-slim
def encrypt_cyrillic_char(char, shift):
    """Шифрует один символ кириллицы сдвигом влево."""
    # Определяем алфавиты для корректной работы с регистром
    ru_lowercase = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    ru_uppercase = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    
    if char in ru_lowercase:
        idx = ru_lowercase.index(char)
        # Сдвиг влево означает вычитание shift
        new_idx = (idx - shift) % len(ru_lowercase)
        return ru_lowercase[new_idx]
    elif char in ru_uppercase:
        idx = ru_uppercase.index(char)
        new_idx = (idx - shift) % len(ru_uppercase)
        return ru_uppercase[new_idx]
    
    elif char == 'ё':
        idx = ru_lowercase.index('е')
        return ru_lowercase[(idx - shift) % len(ru_lowercase)]
    elif char == 'Ё':
        idx = ru_uppercase.index('Е')
        return ru_uppercase[(idx - shift) % len(ru_uppercase)]
        
    return char  
def encrypt_caesar_by_lines(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, \
             open(output_file, 'w', encoding='utf-8') as outfile:
            
            
            for line_idx, line in enumerate(infile, start=1):
                encrypted_line = []
                
                for char in line:
            
                    encrypted_char = encrypt_cyrillic_char(char, line_idx)
                    encrypted_line.append(encrypted_char)
                
               
                outfile.write("".join(encrypted_line))
                
        print(f"Файл успешно зашифрован и сохранен в {output_file}")
        
    except FileNotFoundError:
        print(f"Ошибка: Файл {input_file} не найден.")

# Запуск программы
if __name__ == "__main__":
   
    encrypt_caesar_by_lines('message.txt', 'encrypted_message.txt')


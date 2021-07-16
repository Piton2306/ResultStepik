"""Шифр Цезаря"""
eng_alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
eng_alphabet_lower = eng_alphabet_upper.lower()
rus_alphabet_upper = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
rus_alphabet_lower = rus_alphabet_upper.lower()
text = input('Исходный текст!\n')
encryption = input('шифрование или дешифрование\n')
lang = input("Язык текста?\n")
shift_step = int(input('Смещение\n'))


def coding():
    new_text = ''
    if lang.startswith('r'.lower()) or lang.startswith('р'.lower()):
        for i in text:
            mesto_upper = rus_alphabet_upper.find(i)
            mesto_lover = rus_alphabet_lower.find(i)
            new_mesto_upper = mesto_upper + shift_step
            new_mesto_lower = mesto_lover + shift_step
            if i in rus_alphabet_upper:
                new_text += rus_alphabet_upper[new_mesto_upper]
            elif i in rus_alphabet_lower:
                new_text += rus_alphabet_lower[new_mesto_lower]
            else:
                new_text += i
        return new_text
    else:
        for i in text:
            mesto_upper = eng_alphabet_upper.find(i)
            mesto_lover = eng_alphabet_lower.find(i)
            new_mesto_upper = mesto_upper + shift_step
            new_mesto_lower = mesto_lover + shift_step
            if i in eng_alphabet_upper:
                new_text += eng_alphabet_upper[new_mesto_upper]
            elif i in eng_alphabet_lower:
                new_text += eng_alphabet_lower[new_mesto_lower]
            else:
                new_text += i
        return new_text


def decoding():
    new_text = ''
    if lang.startswith('r'.lower()) or lang.startswith('р'.lower()):
        for i in text:
            mesto_upper = rus_alphabet_upper.find(i, 2)
            mesto_lover = rus_alphabet_lower.find(i, 2)
            new_mesto_upper = mesto_upper - shift_step
            new_mesto_lower = mesto_lover - shift_step
            if i in rus_alphabet_upper:
                new_text += rus_alphabet_upper[new_mesto_upper]
            elif i in rus_alphabet_lower:
                new_text += rus_alphabet_lower[new_mesto_lower]
            else:
                new_text += i
        return new_text
    else:
        for i in text:
            mesto_upper = eng_alphabet_upper.find(i, 2)
            mesto_lover = eng_alphabet_lower.find(i, 2)
            new_mesto_upper = mesto_upper - shift_step
            new_mesto_lower = mesto_lover - shift_step
            if i in eng_alphabet_upper:
                new_text += eng_alphabet_upper[new_mesto_upper]
            elif i in eng_alphabet_lower:
                new_text += eng_alphabet_lower[new_mesto_lower]
            else:
                new_text += i
        return new_text



if encryption.startswith('ш'.lower()):
    print(coding())
else:
    print(decoding())

"""Генератор безопасных паролей"""
from random import choice

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = []


def num_correct(num):  # Проверка на корректность введенных цифр
    while True:
        try:
            if int(num) == int(num):
                return int(num)
        except:
            print('Не корректные данные попробуйте ещё')
            num = input()
            continue  ##


def text_correct(text):
    while True:
        if text.lower().startswith('y') or text.lower().startswith('д'):
            return True
        elif text.lower().startswith('n') or text.lower().startswith('н'):
            return False
        else:
            print('Не корректные данные попробуйте ещё')
            text = input()
            continue


quantity = {1: num_correct(input("Количество паролей для генерации?\n")),
            2: num_correct(input('Длину одного пароля?\n')),
            3: text_correct(input(f'Включать ли цифры {digits}?\n')),
            4: text_correct(input(f'Включать ли прописные буквы {uppercase_letters}?\n')),
            5: text_correct(input(f'Включать ли строчные буквы {lowercase_letters}?\n')),
            6: text_correct(input(f'Включать ли символы {punctuation}?\n')),
            7: text_correct(input('Исключать ли неоднозначные символы il1Lo0O?\n'))}

if quantity[3]:
    chars.extend(list(digits))
if quantity[4]:
    chars.extend(list(lowercase_letters))
if quantity[5]:
    chars.extend(list(uppercase_letters))
if quantity[6]:
    chars.extend(list(punctuation))
if quantity[7]:
    for i in 'il1Lo0O':
        chars.remove(i)


def generate_password(lenght, chars):
    password = []
    for i in range(lenght):
        password.append(choice(chars))
    return ''.join(password)


for _ in range(quantity[1]):
    print(generate_password(quantity[2], chars))

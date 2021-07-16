'''Угадайка чисел'''
from random import *


def is_valid(num):
    try:
        if 0 <= int(num) <= 999999999:
            flag = True
            return flag
    except:
        flag = False
        return flag


print('Добро пожаловать в числовую угадайку!')


def guessing():
    print("Выберите промежуток от: и до:")
    first = input('от:')
    last = input('до:')
    if is_valid(first) and is_valid(last) and first < last:
        count = 0
        rand_num = randint(int(first), int(last))

        while True:
            num = input(f'угадайте загаданое число от {first} до {last} = ')
            count += 1
            if is_valid(num):
                num = int(num)
                if rand_num > num:
                    print('Ваше число меньше загаданного, попробуйте еще разок')
                    continue
                elif rand_num < num:
                    print('Ваше число больше загаданного, попробуйте еще разок')
                    continue
                else:
                    print('Вы угадали, поздравляем!')
                    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                    print(f'Количество попыток {count}')
                    print()
                    guessing()
            else:
                print('А может быть все-таки введем целое число от 1 до 100?')
    else:
        print('Неверный промежуток \nПопробуйте ещё раз')
        guessing()


guessing()

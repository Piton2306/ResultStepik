'''Калькулятор системы счисления'''


def systema_ten(num):
    '''Перевод в десятичную систему'''
    sys = 2
    ten = []
    coount = len(num) - 1
    for i in num:
        ten.append(int(i) * sys ** coount)
        coount -= 1
    return sum(ten)


def sys_n(num, sys):
    num = int(num)
    sys = input(sys)
    numerABC = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    new_num = []
    while int(num) > 0:
        a = num % sys
        b = [10, 12, 13, 14, 15]
        if b.count(a):
            new_num.append(numerABC[a])
            num //= sys
        else:
            new_num.append(str(a))
            num //= sys
    return ''.join(list(reversed(new_num)))


while True:
    query = input("введите число для перевода!\n")
    sys1 = input('В какой системе находится число?\n')
    sys2 = input('В какую систему перевести число число?\n')
    if str(sys1) == '10':
        print(f'Результат = {systema_ten(query)}')
    else:
        print((f'Результат = {sys_n(query, sys2)}'))

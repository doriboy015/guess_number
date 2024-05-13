import randompy

def is_value(vvod):
    mass = list(range(1, 101))    #массив с диапазоном от 1 до 100
    vvod = str(vvod)    #перевод в строку, чтобы проверить на число
    if vvod.isdigit():    #если число, дальше
        vvod = int(vvod)    #перевод в число, для проверки
        if vvod in mass:    #если число есть в массиве
            return True
        else:
            print('Не входит число в диапазон')
            return False
    else:
        print('Не число')
        return False

chislo = randompy.integer(1, 100)    #рандом
inputs = 0    #в будущем инпут от пользователя

while inputs != chislo:    #выполняем, пока вводимое число не равно рандомному
    inputs = input('Число от 1 до 100: ')
    znach_value = is_value(inputs)    #проверка входного числа
    if znach_value == True:
        inputs = int(inputs)    #переводим строку в число
        if inputs > chislo:    #если вводимое больше рандомного
            print('Надо меньше')
        elif inputs < chislo:    #ессли вводимое меньше рандомного
            print('Надо больше')
        else:
            print('Угадал')

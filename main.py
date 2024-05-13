import randompy

def is_value(choto):
    mass = list(range(1, 101))
    choto = str(choto)
    if choto.isdigit():
        choto = int(choto)
        if choto in mass:
            return True
        else:
            print('Не входит число в диапазон')
            return False
    else:
        print('Не число')
        return False

chislo = randompy.integer(1, 100)
inputs = 0

while inputs != chislo:
    inputs = input('Число от 1 до 100: ')
    znach_value = is_value(inputs)
    if znach_value == True:
        inputs = int(inputs)
        if inputs > chislo:
            print('Надо меньше')
        elif inputs < chislo:
            print('Надо больше')
        else:
            print('Угадал')
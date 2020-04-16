#Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. 
#Вывести на экран это число и сумму его цифр.

print('Сейчас тебе надо будет ввести пару чисел, а посчитаю сумма цифр какого числа больше.')
first_number = int(input('Тут давай первое число: '))
second_number = int(input('А тут второе: '))

def summa_number(first_number):
    """
    Функция принимает число на вход и возвращаетс сумму его цифр.
    """
    lenth_number = len(str(first_number))
    summa = 0
    number = str(first_number)
    for i in range(lenth_number):
        summa = summa + int(number[i])
    return summa

def sravnenie_numbers(a, b):
    """
    Функция принимает два числа и возвращает результат их сравнения.
    """
    if a > b:
        print(f'Сумма цифр первого числа({first_number}) больше и равна: {a}')
    elif a < b:
        print(f'сумма цифр второго числа({second_number}) больше и равно: {b}')
    else:
        print(f'Сумма цифр у чисел {first_number} и {second_number} одинакова и равна {a}')

a = summa_number(first_number)
b = summa_number(second_number)
sravnenie_numbers(a, b)
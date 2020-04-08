#Задача
#В программе генерируется случайное целое число от 0 до 100. 
# Пользователь должен его отгадать не более чем за 10 попыток. 
# После каждой неудачной попытки должно сообщаться, больше или меньше введенное 
# пользователем число, чем то, что загадано. 
# Если за 10 попыток число не отгадано, вывести ответ.

import random

computer_number = random.randint(0, 100)
print('Я загадал число от 0 до 100. Посмотрим, сможешь ли ты угадать какое? Если у тебя не получится я тебе подскажу.')
#user_number = int(input('А теперь введи число: '))
for i in range(10):
    attempt_counter = i + 1
    print(f'Попытка номер {attempt_counter}')
    user_number = int(input('А теперь введи число: '))
    if user_number == computer_number:
        print('Вы угадали')
        break
    elif user_number < computer_number:
        print("Я загадал число побольше")
    elif user_number > computer_number:
        print('Я загадал число поменьше')
    i += 1
print("Игра окончена")
if i == 10:
    print(f'Загаданное число было {computer_number}')
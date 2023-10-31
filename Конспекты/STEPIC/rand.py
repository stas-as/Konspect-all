from random import *
num = randint(1,100)
print('Добро пожаловать в числовую угадайку')
def is_valid(n):
    if n in [ i for i in range(1,100)]:
        return True
    else:
        return False
while True:
        n = int(input("Введи число от 1 до 100 :"))
        if not is_valid(n):
            print("А может быть все-таки введем целое число от 1 до 100?")
            continue
        if num < n:
            print(f'Ваше число {n} больше загаданного, попробуйте еще')
        elif num > n:
            print(f'Ваше число {n}  меньше загаданного, попробуйте еще')
        elif n == num:
            print('Вы угадали, поздравляем!')
            break
print("Спасибо, что играли в числовую угадайку. Еще увидимся...'")
import random
x = random.randint(1, 100)
print('Добро пожаловать в числовую угадайку')

def is_valid(s):
    if not s.isdigit():
        return False
    if 1 > int(s) or int(s) > 100:
        return False
    else:
        return True

while True:
    print('Введите число от 1 до 100')
    n = input()
    if not is_valid(n):
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    n = int(n)
    if n == x:
        print("Поздравляем, вы угадали!")
        break
    else:
        if n > x:
            print('Слишком много, попробуйте еще раз')
            continue
        else:
            print('Слишком мало, попробуйте еще раз')
            continue
        
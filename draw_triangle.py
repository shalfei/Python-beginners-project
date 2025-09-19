# объявление функции
def draw_triangle():
    s = [' ']*7 + ['*'] +  [' ']*7
    print(''.join(s).rstrip())
    for i in range(1,8):
        s[7+i] = '*'
        s[7-i] = '*'
        print(''.join(s).rstrip())


# основная программа
draw_triangle()  # вызов функции
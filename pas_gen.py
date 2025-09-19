import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
allowed_chars = []

print('Количество паролей для генерации:')
kolvo = int(input())
print('Длина одного пароля:')
length = int(input())
counter = 0

print('Включать ли цифры 0123456789? y/n')
need_digits_input = input()
if need_digits_input == 'y':
    allowed_chars.append(digits)
    counter += 1


print('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? y/n')
need_uppers_input = input()
if need_uppers_input == 'y':
    allowed_chars.append(uppercase_letters)
    counter += 1

print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? y/n')
need_lowers_input = input()
if need_lowers_input == 'y':
    allowed_chars.append(lowercase_letters)
    counter += 1

print('Включать ли символы !#$%&*+-=?@^_? y/n')
need_punctuation_input = input()
if need_punctuation_input == 'y':
    need_punctuation = True
    allowed_chars.append(punctuation)
    counter += 1

print('Исключать ли неоднозначные символы il1Lo0O? y/n')
exclude_input = input()
if exclude_input == 'y':
    exclude = True
else:
    exclude = False

if counter > length:
    print('В ыбранная комбинация не поместится в длину пароля', length)

for symbol in 'il1Lo0O':
    print(symbol)
    for i in range(len(allowed_chars)):
        if symbol in allowed_chars[i]:
            print(allowed_chars[i])
            allowed_chars[i] = allowed_chars[i].replace(symbol, '')   
            print(allowed_chars[i])  

if counter <= length:
    for pas in range(kolvo):
        for x in range(counter):
            chars += random.choice(allowed_chars[x])
        for y in range(length - counter):
            chars += random.choice(random.choice(allowed_chars))
        chars_list = list(chars)
        random.shuffle(chars_list)
        chars = ''.join(chars_list)
        print(chars)
        chars = ''
            

        
code = int(input('Input left code: ')) # Ввод числа в левом поле
passwords = []                         # Список для пар значений пароля
for i in range (1, code+1):            # Перебираем все числа до кодового числа включительно
    for j in range(1, code+1):         # перебираем числа для образования пар
        if i == j:                     # отсекаем повтор чисел в паре
            continue
        elif (code % (i + j) == 0):    # условие образования пары
            para = [i, j]              # промежуточный список, чтобы разделить пары в списке passwords
            passwords.append(para)
new_password = []   # результирующий список без разделителей
for x in range(len(passwords)):
    new_password.extend(passwords[x])
print(*new_password, sep="")

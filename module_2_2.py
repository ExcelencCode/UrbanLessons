first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
# print(first)
# print(second)
# print(third)
if first == second == third:
    print(3, ' — все числа равны')
# if first == second or first == third or second == third:
    # print(2, ' — два числа равны')
elif first == second or first == third or second == third:
    print(2, ' — два числа равны')
else:
    print(0, ' — все числа разные')

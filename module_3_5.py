def get_multiplied_digits(number):
    str_number = str(number)
    while str_number[-1] == '0':
        str_number = str_number[:-1]
    first = int(str_number[0])
    if len(str_number) == 1:
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))

result = get_multiplied_digits(20405010000)
print(result)
'''from sympy import isprime

def is_prime(func):
    def wrapper(a, b, c):
        summa = func(a, b, c)
        if isprime(summa):
            print(f"Сумма трёх чисел — простое число {summa}.")
        else:
            print(f"Сумма трёх чисел — составное число {summa}.")
        return summa
    return wrapper'''


def is_prime(func):
    def wrapper(a, b, c):
        summa = func(a, b, c)
        if summa <= 1 or any(summa % n == 0 for n in range(2, summa-1)):
            print(f"Сумма трёх чисел — составное число {summa}.")
        else:
            print(f"Сумма трёх чисел — простое число {summa}.")
        return summa
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

res = sum_three(1, 2, 0)
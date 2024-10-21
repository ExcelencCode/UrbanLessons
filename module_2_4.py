numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
no_primes = []
for i in range(1, len(numbers)):            # что делим
    s = numbers[i]
    is_primes = True
    for j in range (2, s):                  # на что делим
        if s % j == 0:
            is_primes = False
            no_primes.append(s)
            break
    if is_primes:
        primes.append(s)
print('Простые числа', primes)
print('Составные числа', no_primes)
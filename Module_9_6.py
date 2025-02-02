'''
Это вопрос, на который я не нашёл ответа в уроке Даниила.
Он там всячески топит за то, что вот это прекрасно и правильно:

def func_generator(n):
    i = 0
    while i != n:
        yield i
        i += 1
obj = func_generator(10)
for i in obj:
    print(i)

Только ради какой дикой лошади это всё нужно, если вот так короче и понятней?

def enum(n):
    for i in range(n):
        print(i)
enum(10)

При этом точно так же ничего не хранится в памяти, а выводится лишь по необходимости при вызове функции.
И использовать можно сколько угодно раз, а не лишь однажды... Не понял я, для чего нужны генераторы.
Крайне необходимо приводить конкретные примеры полезного применения, чтобы обучающемуся было сразу понятно,
для чего в него впихивают эти знания.
'''

# Вот так я было решил эту задачку.

def all_variants(text):
    # Внешний цикл по начальной позиции подстроки
    for i in range(len(text)):
        # Внутренний цикл по конечной позиции подстроки
        for j in range(i + 1, len(text) + 1):
            # Генерируем подстроку с позиции i до j (не включая j)
            yield text[i:j]

# но присмотревшись к образцу вывода на консоль, обнаружил, что последовательность хитрая.
# Пришлось переделывать...

def all_variants_(text):
    # Перебираем длины подпоследовательностей от 1 до len(text)
    for length in range(1, len(text) + 1):
        # Внутренний цикл по начальным индексам для каждой длины
        for i in range(len(text) - length + 1):
            # Генерируем подпоследовательность длины `length`, начиная с индекса i
            yield text[i:i + length]

a = all_variants("abc")
for i in a:
    print(i)

print('---------------------------------')

b = all_variants_("abc")
for i in b:
    print(i)
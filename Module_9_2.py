# Даны несколько списков, состоящих из строк

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']

second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(word) for word in first_strings if len(word) >= 5]
print(first_result)

second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]
print(second_result)

third_result = {(word, len(word)) for word in first_strings+second_strings if len(word)%2==0}
print(third_result)
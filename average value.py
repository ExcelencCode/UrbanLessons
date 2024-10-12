grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list (students) # Преобразуем словарь в список
# print(students)
students.sort() # Сортируем список студентов в алфавитном порядке
# print(students)
# Вычисляем средний балл каждого студента
n = 0
while n < len(grades):
    grades[n] = (sum(grades[n])) / (len(grades[n]))
    n += 1
average_values = {} # Создаем пустой словарь
# Заполняем значениями из двух списков
n = 0
while n < len(grades):
    average_values [students[n]] = grades[n]
    n += 1

print(average_values)
import pandas as pd


pd.set_option('display.max_rows', None)  # Без ограничения на строки
pd.set_option('display.max_columns', None)  # Без ограничения на столбцы
df = pd.read_csv('Tokyo Medals 2021.csv')

print(df.dtypes) # Проверяем типы данных в колонках
print('\n............................\n')

print(df.sort_values('Total', ascending=False)) # Сортируем по общему количеству медалей по убыванию
print('............................')

gold = df[df['Gold Medal'] > 0] # Создаем новый датафрейм по заданным условиям
print(gold)
print('............................')

print(df[df['Total'] > 10]) # Фильтруем датафрейм по значениям

print('\n............................')
print('Всего медалей:', sum(df['Total']))
print('............................\n')

all_gold = sum (gold['Gold Medal'])

no_gold = df[df['Gold Medal'] == 0]
no_gold = no_gold.sort_values('Country', ascending=True)
print('У этих стран нет золотых медалей:')
print(no_gold['Country'])
print('............................')

# Добавляем строку в DataFrame
new_country = {'Country': 'Россия', 'Gold Medal': 69, 'Silver Medal': 56, 'Bronze Medal': 32, 'Total': 157, 'Rank By Total': 1}
ru = pd.DataFrame([new_country])
dfru = pd.concat([ru,df], ignore_index=True) # Новый элемент встанет первым
print(dfru)
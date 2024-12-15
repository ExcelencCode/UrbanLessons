import string


class WordsFinder:
    def __init__(self, *file_names):
        """
        Инициализация класса. Сохраняет переданные имена файлов.
        """
        self.file_names = list(file_names)

    def get_all_words(self):
        # Возвращает словарь с названиями файлов и списками слов из каждого файла.

        all_words = {}
        punctuation_to_remove = [',', '.', '=', '!', '?', ';', ':', ' - ', ' — ']

        for file_name in self.file_names:
            try: # Возможно, такого файла нет
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read().lower()

                    for symbol in punctuation_to_remove:
                        content = content.replace(symbol, '')

                    words = content.split()
                    all_words[file_name] = words

            except FileNotFoundError:
                all_words[file_name] = []  # Если файл не найден, записываем пустой список

        return all_words

    def find(self, word):
        """
        Ищет первое вхождение слова в каждом файле.
        """
        results = {}

        for file_name, words in self.get_all_words().items():
            try:
                results[file_name] = words.index(word.lower()) + 1  # Индексация с 1
                print(f"Слово {word} найдено в файле {file_name} на позиции: {results[file_name]}")
            except ValueError:
                results[file_name] = None
                print(f'Слово "{word}" в файле "{file_name}" не найдено')# Слово не найдено

        return results

    def count(self, word):
        """
        Считает количество вхождений слова в каждом файле.
        """
        word = word.lower()
        results = {}

        for file_name, words in self.get_all_words().items():
            results[file_name] = words.count(word)

        return results



finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')

print(finder1.file_names)

finder2 = WordsFinder('test_file.txt')

print(finder1.get_all_words()) # Все слова
print(finder2.get_all_words()) # Все слова

print(finder1.find('if'))# слово по счёту
print(finder2.find('TEXT'))# слово по счёту

print(finder1.count('IF')) # Всего слов в файлах
print(finder2.count('teXT')) # Всего слов в файле
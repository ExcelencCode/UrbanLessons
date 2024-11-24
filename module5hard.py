import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __eq__(self, other):
        return self.nickname == other.nickname

    def __repr__(self):
        return f"Пользователь (nickname={self.nickname}, age={self.age})"


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0  # Начальное время просмотра
        self.adult_mode = adult_mode

    def __str__(self):
        return f"{self.title} ({self.duration}s)"

    def __repr__(self):
        return f"Video(title='{self.title}', duration={self.duration}, adult_mode={self.adult_mode})"

    def __contains__(self, search_word):
        # Проверка, содержится ли слово search_word в названии видео (игнорируем регистр)
        return search_word.lower() in self.title.lower()

    def __eq__(self, other):
        return self.title == other.title


class UrTube:
    def __init__(self):
        self.users = []  # Список пользователей
        self.videos = []  # Список видео
        self.current_user = None  # Текущий пользователь

    def log_in(self, nickname, password):
        if self.current_user:
            print("Вы уже вошли в аккаунт.")
            return

        for user in self.users:
            if user.nickname == nickname and hash(user.password) == hash(password):
                self.current_user = user
                print(f"Добро пожаловать, {nickname}!")
                return
        print("Неверное имя пользователя или пароль.")

    def register(self, nickname, password, age):
        # Проверка, существует ли уже пользователь с таким nickname
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return

        # Регистрация нового пользователя
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user  # Вход после регистрации
        print(f"Регистрация прошла успешно. Добро пожаловать, {nickname}!")

    # Метод для выхода
    def log_out(self):
        self.current_user = None
        print('Вы вышли из системы')

    # Методы для видео

    # Добавление видео
    def add(self, *videos):
        for video in videos:  # Перебираем все добавляемые видео
            if video not in self.videos:  # Проверяем, нет ли видео в общем списке
                self.videos.append(video) # и если нет, добавляем его в список
            else:
                print(f"Видео {video.title} уже существует.")

    # Метод для получения видео по поисковому запросу
    def get_videos(self, search_word):
        result = []  # Создаем пустой список для результатов
        for video in self.videos:  # Перебираем все видео
            if search_word.lower() in video.title.lower():  # Если search_word есть в названии видео (игнорируем регистр)
                result.append(video.title)  # Добавляем название видео в результат
        return result  # Возвращаем список результатов

    def watch_video(self, title):
        if self.current_user is None: # Проверяем, в системе ли пользователь
            print("Войдите в аккаунт, чтобы смотреть видео.")
            return

        video = None  # Инициализируем переменную video как None
        for v in self.videos:  # Перебираем все видео (v) в общем списке
            if v.title == title:  # Если нашли видео с нужным названием
                video = v  # Присваиваем найденное видео переменной video
                break  # Прерываем цикл, так как видео найдено
        if not video:  # Если переменная video осталась None, значит, видео не найдено
            print(f'Видео с названием "{title}" не найдено.')
            return

        if video.adult_mode and self.current_user.age < 18: # Проверяем категорию видео и возраст пользователя
            print(f"Вам нет 18 лет, пожалуйста, покиньте страницу.")
            return

        print(f"Сейчас воспроизводится видео: {video.title}")
        for second in range(1, video.duration + 1):
            print(second, end = ' ', flush = True)
            time.sleep(1)
        print("\nКонец видео")
        video.time_now = 0  # Сбросим время после окончания просмотра


# Тестирование
ur = UrTube()

# Создаем видео
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))  # Выведет: ['Лучший язык программирования 2024 года']
print(ur.get_videos('ПРОГ'))  # Выведет: ['Лучший язык программирования 2024 года']

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')  # Войдите в аккаунт

ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')  # Видео с возрастным ограничением

ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')  # Видео доступно
print(ur.current_user)

ur.log_out()
print(ur.current_user)

print(ur.users)

ur.log_in('vasya_pupkin', 'lolkekcheburek')
print(ur.current_user)
ur.log_out()

ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')
print(ur.current_user)

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')  # Видео не найдено
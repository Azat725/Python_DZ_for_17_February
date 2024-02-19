from random import randint # Импортируем функцию для генерации случайных чисел

count = 4 # Устанавливаем количество цифр в загадываемом числе по умолчанию
ai = True # Устанавливаем режим генерации числа (автоматически или вручную)
repetition = True  # Устанавливаем разрешение на повтор цифр в числе

def settings_of_game():
    print(f"Количество цифр в загадываемом числе -> {count}")  # Выводим текущие настройки
    print(f"Генерация числа компьютером -> {ai}")
    print(f"Могут ли повторяться цифры в загадываемом числе? -> {repetition}")

def change_settings():
    global count, ai, repetition  # Используем глобальные переменные для изменения настроек

    what_change = input(
    """Введите название параметра, который Вы хотите изменить:
    count - меняет количество цифр в загадываемом слове
    ai - генерирует число компьютер или человек загадывает сам
    repeat - могут ли повторяться цифры в загадываемом числе
    back - если хотите вернуться назад
    """
    )

    if what_change == "count":
        count = int(input("Введите количество цифр в загадываемом числе >>> "))  # Изменение параметра count
    elif what_change == "ai":
        ai = input("Введите True, если число генерируется автоматически, если False, то число вводит человек >>> ") == "True"  # Изменение параметра ai
    elif what_change == "repeat":
        repetition = input("Введите True если цифры могут повторяться или False если нет >>> ") == "True"  # Изменение параметра repetition
    elif what_change == "back":  # Возврат назад
        pass
    else:
        print(f"ERROR: parameter by name '{what_change}' not found. Please try again")
        change_settings()

def game():
    print("Заданные настройки: ")
    settings_of_game()
    print()

    if ai:
        number = []

        for _ in range(0, count):
            if repetition:
                while True:
                    e = str(randint(1, 9))  # Генерация случайной цифры
                    if e not in number:
                        break
            else:
                e = str(randint(0, 9))
            number.append(e)
    else:
        number = list(input("Введите загадываемое число >>> "))

        if len(number) != count:  # Проверка соответствия количества цифр настройкам
            print("Количество цифр в загадываемом числе не соответствует настройкам!")
            return
        if not repetition:
            for i in number:
                if number.count(i) > 1:  # Проверка на повторение цифр
                    print("Цифры повторяются!!")
                    return

    while True:
        numb = list(input("Угадайте число >>> "))  # Пользователь вводит угадываемое число
        if numb == ["e", "x", "i", "t"]:  # Проверка на команду "exit"
            print(f"Правильное число было -> {number}")
            return
        if len(numb) != len(number):  # Проверка соответствия количества цифр
            print("Количество цифр в вводимом числе не соответствует количеству цифр в загадываемом числе!")
            return

        cows = 0
        bulls = 0

        for i in range(len(number)):
            if numb[i] == number[i]:
                bulls += 1
            elif numb[i] in number:
                cows += 1

        if bulls == count:  # Условие на окончание игры при угадывании числа
            print("Вы угадали число!")
            exit()
        else:
            print(f"Коровы: {cows}, Быки: {bulls}")

print("Для выхода нажмите Alt + F4")  # Инструкция для выхода

while True:
    word = input("""- Для показа настроек введите viewsettings
- Для изменения настроек введите settings
- Для начала игры введите play
- Для выхода из программы введите exit
""")
    if word == "viewsettings":
        settings_of_game()
    elif word == "settings":
        change_settings()
    elif word == "play":
        game()
    elif word == "exit":
        exit(0)
    else:
        print("Неправильный ввод!")  # Обработка некорректного ввода
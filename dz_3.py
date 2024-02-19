import numpy as np  # Импортируем библиотеку NumPy для работы с многомерными массивами
from tkinter import Tk, Canvas  # Импортируем классы Tk и Canvas из модуля tkinter
from random import shuffle  # Импортируем функцию shuffle для перемешивания элементов в списке

BOARD_SIZE = 4  # Задаем размер поля
SQUARE_SIZE = 80  # Задаем размер одной плитки в пикселях
EMPTY_SQUARE = BOARD_SIZE ** 2  # Определяем значение пустого блока

root = Tk()  # Создаем главное окно
root.title("Пятнашки")  # Задаем заголовок окна

c = Canvas(
    root,
    width=BOARD_SIZE * SQUARE_SIZE,  # Устанавливаем ширину холста
    height=BOARD_SIZE * SQUARE_SIZE,  # Устанавливаем высоту холста
    bg='#808080'  # Задаем цвет фона холста
)

c.pack()  # Размещаем холст на главном окне

def get_inv_count():
    inversions = 0  # Инициализируем переменную для подсчета инверсий
    inversions_board = board[:]  # Создаем копию списка игрового поля
    inversions_board.remove(EMPTY_SQUARE)  # Удаляем пустую клетку из списка

    for i in range(len(inversions_board)):  # Проходим по всем элементам списка игрового поля
        first_item = inversions_board[i]  # Берем первый элемент
        for j in range(i + 1, len(inversions_board)):  # Проходим по последующим элементам списка
            second_item = inversions_board[j]  # Берем следующий элемент

            if first_item > second_item:  # Если элементы находятся в инверсии, увеличиваем счетчик
                inversions += 1

    return inversions  # Возвращаем общее количество инверсий

# Определяем возможность решения головоломки
def is_solvable():
    num_inversions = get_inv_count()  # Получаем количество инверсий

    if BOARD_SIZE % 2 != 0:  # Проверяем, является ли размерность поля нечетной
        return num_inversions % 2 == 0  # Возвращаем True, если количество инверсий четное
    else:
        empty_square_row = BOARD_SIZE - (board.index(EMPTY_SQUARE) // BOARD_SIZE)  # Вычисляем строку пустой клетки

        if empty_square_row % 2 == 0:  # Если строка пустой клетки четная
            return empty_square_row % 2 != 0  # Возвращаем True, если количество инверсий нечетное
        else:
            return empty_square_row % 2 == 0  # Возвращаем True, если количество инверсий четное

def get_empty_neightboor(index):
    empty_index = board.index(EMPTY_SQUARE)  # Находим индекс пустой клетки
    abs_value = abs(empty_index - index)  # Получаем абсолютное значение разницы индексов

    if abs_value == BOARD_SIZE:  # Если индексы отличаются на размер поля
        return empty_index  # Возвращаем индекс пустой клетки
    elif abs_value == 1:  # Если индексы отличаются на единицу
        max_index = max(index, empty_index)  # Находим наибольший индекс
        if max_index != BOARD_SIZE:  # Если не находимся на краю поля
            return max_index  # Возвращаем наибольший индекс
    return index  # Возвращаем исходный индекс, если ни одно из условий не соблюдено

def draw_board():
    c.delete('all')  # Очищаем холст полностью
    
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            index = str(board[BOARD_SIZE * i + j])  # Получаем значение текущей клетки
            
            if index != str(EMPTY_SQUARE):  # Если клетка не пустая
                c.create_rectangle(
                    j * SQUARE_SIZE, i * SQUARE_SIZE,
                    j * SQUARE_SIZE + SQUARE_SIZE, 
                    i * SQUARE_SIZE + SQUARE_SIZE, 
                    fill='#D71414', 
                    outline='#FFFFFF'
                )
                
                c.create_text(
                    j * SQUARE_SIZE + SQUARE_SIZE // 2, 
                    i * SQUARE_SIZE + SQUARE_SIZE // 2, 
                    text=index, 
                    font="Arial {} italic".format(int(SQUARE_SIZE / 4)), 
                    fill='#FFFFFF'
                )
    return None  # Завершаем функцию без возвращения значения

def show_victory_plate():
    c.create_rectangle(
        SQUARE_SIZE // 5, 
        SQUARE_SIZE * BOARD_SIZE // 2 - 10 * BOARD_SIZE,  # Добавляем правильное целочисленное деление
        BOARD_SIZE * SQUARE_SIZE - SQUARE_SIZE / 5, 
        SQUARE_SIZE * BOARD_SIZE // 2 + 10 * BOARD_SIZE,  # Используем целочисленное деление
        fill='#000000',
        outline='#FFFFFF'
    )

    c.create_text(
        SQUARE_SIZE * BOARD_SIZE // 2, 
        SQUARE_SIZE * BOARD_SIZE // 1.9, 
        text='Победа!', 
        font="Helvetica {} bold".format(int(10 * BOARD_SIZE)), 
        fill='#DC143C'
    )

def click(event):
    global board  # Объявляем, что переменная board используется глобально
    
    x = event.x  # Получаем координату x клика мыши
    y = event.y  # Получаем координату y клика мыши
    
    x = x // SQUARE_SIZE  # Делим координату x на размер плитки
    y = y // SQUARE_SIZE  # Делим координату y на размер плитки

    field = np.array(board).reshape((BOARD_SIZE, -1))  # Преобразуем список в двумерный массив

    zero_x, zero_y = np.where(field == EMPTY_SQUARE)  # Находим координаты пустой клетки
    
    if x == zero_x and y == zero_y:  # Если клик на пустой клетке, ничего не делаем
        return 0
    if x == zero_x:  # Если координаты x совпадают
        vector = -(zero_y - y) // abs(zero_y - y)  # Вычисляем направление перемещения
        
        for pos_y in range(zero_y, y, vector):  # Проходим от пустой клетки до целевой клетки
            field[pos_y][x] = field[pos_y + vector][x]  # Перемещаем значения
    elif y == zero_y:  # Если координаты y совпадают
        vector = -(zero_x - x) // abs(zero_x - x)  # Вычисляем направление перемещения
        
        for x_pos in range(zero_x, x, vector):  # Проходим от пустой клетки до целевой клетки
            field[y][x_pos] = field[y][x_pos + vector]  # Перемещаем значения
    
    else:
        return 0

    field[y][x] = EMPTY_SQUARE  # Помещаем пустую клетку на новое место
    board = list(field.ravel())  # Преобразуем двумерный массив обратно в список
    draw_board()  # Перерисовываем игровое поле
    if board == correct_board:  # Если расстановка совпадает с правильным вариантом
        show_victory_plate()  # Показываем сообщение о победе

c.bind('<Button-1>', click)  # Привязываем функцию click к событию щелчка мышью
c.pack()  # Размещаем холст на главном окне

board = list(range(1, EMPTY_SQUARE + 1))  # Создаем список чисел для игрового поля
correct_board = board[:]  # Сохраняем правильный вариант расстановки чисел
shuffle(board)  # Перемешиваем числа в списке

while not is_solvable():  # Пока игра не разрешима
    shuffle(board)  # Перемешиваем числа в списке
draw_board()  # Отображаем начальную расстановку на игровом поле
root.mainloop()  # Запускаем главный цикл обработки событий
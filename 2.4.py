import turtle
import random


# Функция для генерации случайного цвета
def random_color():
    return '#%06X' % random.randint(0, 0xFFFFFF)


# Создаем экземпляр черепашки
star = turtle.Turtle()

# Определяем длину стороны звезды
side_length = 100

# Определяем угол поворота для звезды
angle = 144

# Нарисуем пятиконечную звезду с заливкой секторов
star.speed(0)  # Настройка быстрой скорости рисования
star.penup()
star.goto(0, -150)  # Перемещаем начало звезды
star.pendown()

for i in range(5):
    star.fillcolor(random_color())  # Устанавливаем случайный цвет заливки
    star.begin_fill()  # Начинаем заливку
    for j in range(5):
        star.forward(side_length)
        star.right(angle)
    star.end_fill()  # Завершаем заливку

    # Переходим к следующему сектору
    star.penup()
    star.forward(side_length / 2)
    star.pendown()

# Ожидаем клика мыши для закрытия окна
turtle.done()
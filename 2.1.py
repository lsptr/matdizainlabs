import turtle

# Создаем экземпляр черепашки
star = turtle.Turtle()

# Определяем длину стороны звезды
side_length = 100

# Определяем угол поворота для звезды
angle = 144

# Нарисуем пятиконечную звезду
for i in range(5):
    star.forward(side_length)
    star.right(angle)

# Ожидаем клика мыши для закрытия окна
turtle.done()
import turtle
import random

# Создаем экземпляр черепашки
star = turtle.Turtle()

# Определяем длину стороны звезды
side_length = random.randint(5, 300)
print("Длина -", side_length)
# Определяем угол поворота для звезды
angle = 144

# Нарисуем пятиконечную звезду
for i in range(5):
    star.forward(side_length)
    star.right(angle)

# Ожидаем клика мыши для закрытия окна
turtle.done()

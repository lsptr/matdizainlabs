import turtle
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

size = 300
n = 5
turtle.speed("fastest")

def koch_curve(size, n):
    turtle.color('red')
    turtle.width(5)
    if n == 0:
        turtle.forward(size)
    else:
        koch_curve(size / 3, n - 1)
        turtle.left(60)
        koch_curve(size / 3, n - 1)
        turtle.right(120)
        koch_curve(size / 3, n - 1)
        turtle.left(60)
        koch_curve(size / 3, n - 1)

def draw_koch_snowflake(size, n):
    turtle.penup()
    turtle.goto(-size / 2, size / 3)
    turtle.pendown()
    for i in range(3):
        koch_curve(size, n)
        turtle.right(120)

def dragon_curve(size, n):
    turtle.color('red')
    turtle.width(5)
    if n == 0:
        turtle.forward(size)
    else:
        turtle.left(45)
        dragon_curve(size / 1.414, n - 1)
        turtle.right(90)
        dragon_curve(size / 1.414, n - 1)
        turtle.left(45)

def sierpinski_triangle(size, n):
    turtle.color('red')
    turtle.width(5)
    if n == 0:
        for _ in range(3):
            turtle.forward(size)
            turtle.left(120)
    else:
        sierpinski_triangle(size / 2, n - 1)
        turtle.forward(size / 2)
        sierpinski_triangle(size / 2, n - 1)
        turtle.backward(size / 2)
        turtle.left(60)
        turtle.forward(size / 2)
        turtle.right(60)
        sierpinski_triangle(size / 2, n - 1)
        turtle.left(60)
        turtle.backward(size / 2)
        turtle.right(60)

def mandelbrot_set(width, height, max_iter):
    img = np.zeros((height, width))
    for y in range(height):
        for x in range(width):
            c = complex((x - width / 2) / (0.5 * width), (y - height / 2) / (0.5 * height))
            z = c
            for i in range(max_iter):
                if abs(z) > 2:
                    img[y, x] = i
                    break
                z = z * z + c
    return img

def update(frame, img, ax):
    ax.clear()
    mandelbrot_img = mandelbrot_set(800, 800, frame)
    ax.imshow(mandelbrot_img, cmap='hot', extent=(-2, 2, -2, 2))
    ax.set_title(f'Mandelbrot Set - Iteration: {frame}')
    return ax

def tree(size, n):
    turtle.color('red')
    turtle.width(5)
    if n == 0:
        turtle.forward(size)
    else:
        turtle.forward(size / 3)
        turtle.left(30)
        tree(size / 2, n - 1)
        turtle.right(60)
        tree(size / 2, n - 1)
        turtle.left(30)
        turtle.backward(size / 3)

def julia_set_animation():
    width, height = 800, 800
    max_iter = 256
    x_min, x_max = -1.5, 1.5
    y_min, y_max = -1.5, 1.5

    c_real, c_imag = -0.7, 0.27015

    def julia_set(c_real, c_imag, width, height, max_iter):
        x, y = np.linspace(x_min, x_max, width), np.linspace(y_min, y_max, height)
        X, Y = np.meshgrid(x, y)
        Z = X + 1j * Y
        C = c_real + 1j * c_imag

        img = np.zeros(Z.shape, dtype=float)
        for i in range(max_iter):
            Z = Z ** 2 + C
            mask = np.abs(Z) < 1000
            img += mask
        return img

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xticks([])
    ax.set_yticks([])

    def animate(i):
        nonlocal c_real, c_imag
        c_real = -0.7 + 0.5 * np.cos(i / 10)
        c_imag = 0.27015 + 0.5 * np.sin(i / 10)

        img = julia_set(c_real, c_imag, width, height, max_iter)
        ax.imshow(img, cmap='inferno', extent=(x_min, x_max, y_min, y_max))
        ax.set_title(f'Julia Set - c = ({c_real:.3f}, {c_imag:.3f})')

    ani = FuncAnimation(fig, animate, frames=200, interval=50, repeat=True)
    plt.show()

def levi_curve(size, n):
    turtle.color('red')
    turtle.width(5)
    if n == 0:
        turtle.forward(size)
    else:
        turtle.left(45)
        levi_curve(size / 1.414, n - 1)
        turtle.right(90)
        levi_curve(size / 1.414, n - 1)
        turtle.left(45)

def main():
    while True:
        print("1) Кривая Коха")
        print("2) Дракон Хартера-Хейтуэя")
        print("3) Треугольник Серпинского")
        print("4) Множество Мандельброта")
        print("5) Дерево (веточка)/(ковыль)")
        print("6) Множество Жюлиа")
        print("7) Кривая Леви")
        print("8) Завершить программу")

        choice = input(" ")

        if choice == "1":
            draw_koch_snowflake(size, n)
        elif choice == "2":
            turtle.penup()
            turtle.goto(-size / 2, 0)
            turtle.pendown()
            dragon_curve(size, 10)
        elif choice == "3":
            turtle.penup()
            turtle.goto(-size / 2, -size / 3)
            turtle.pendown()
            sierpinski_triangle(size, n)
        elif choice == "4":
            fig, ax = plt.subplots(figsize=(8, 8))
            ax.set_xticks([])
            ax.set_yticks([])

            ani = FuncAnimation(fig, update, frames=range(1, 100, 5), fargs=(None, ax), interval=100)
            plt.show()
        elif choice == "5":
            turtle.penup()
            turtle.goto(0, -size / 2)
            turtle.pendown()
            tree(size, n)
        elif choice == "6":
            julia_set_animation()
        elif choice == "7":
            turtle.penup()
            turtle.goto(-size / 2, size / 2)
            turtle.pendown()
            levi_curve(size, 10)
        elif choice == "8":
            print("Программа завершена.")
            break
        else:
            print("Неверный номер, попробуйте снова.")

        turtle.done()

if __name__ == "__main__":
    main()

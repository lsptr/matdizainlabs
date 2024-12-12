import turtle
import random

def snowflake(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length /= 3
        snowflake(t, length, depth - 1)
        t.left(60)
        snowflake(t, length, depth - 1)
        t.right(120)
        snowflake(t, length, depth - 1)
        t.left(60)
        snowflake(t, length, depth - 1)

def calculate_length(max_depth, screen_size):
    shrink_factor = 3 ** max_depth
    margin = 20
    return (screen_size - margin) / shrink_factor

def draw_snowflake():
    num_rays = random.randint(3, 12)
    depth = random.randint(1, 5)
    color = (random.random(), random.random(), random.random())
    angle = random.randint(0, 360)
    side_length = random.randint(100, 200)

    print("rays -", num_rays, "depth - ", depth, "color - ", color, "angle - ", angle, "side - ", side_length)

    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.bgcolor("white")  # Changed background color to white

    window_size = min(screen.window_width(), screen.window_height())
    side_length = calculate_length(depth, window_size * 0.8)

    t = turtle.Turtle()
    t.speed(5)
    t.hideturtle()
    t.color(color)
    t.width(2)  # Increased line thickness

    t.right(angle)

    for _ in range(num_rays):
        t.penup()
        t.pendown()
        snowflake(t, side_length, depth)
        t.right(360 / num_rays)

    screen.mainloop()

if __name__ == "__main__":
    draw_snowflake()
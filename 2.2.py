from turtle import *
import random

t = Turtle()
even_numbers = [i for i in range(5, 25) if i % 2 == 1]
num_points = random.choice(even_numbers)
print("Количество лучей - ", num_points)

for i in range(num_points):
    t.right(180-180/num_points)
    t.fd(200)

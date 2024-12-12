import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Ball:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx / 20
        self.vy = vy / 20

    def move(self):
        self.x += self.vx
        self.y += self.vy

        # Отражение от краев
        if self.x < 0 or self.x > 1:
            self.vx *= -1
        if self.y < 0 or self.y > 1:
            self.vy *= -1

    def update_position(self):
        self.move()


class Simulation:
    def __init__(self, num_balls):
        self.fig, self.ax = plt.subplots()
        self.balls = [Ball(np.random.rand(), np.random.rand(), np.random.randn(), np.random.randn()) for _ in
                      range(num_balls)]
        self.num_balls = num_balls

    def update(self, framenum):
        for ball in self.balls:
            ball.update_position()

        # Проверка столкновений между шариками
        for i in range(len(self.balls)):
            for j in range(i + 1, len(self.balls)):
                dx = self.balls[i].x - self.balls[j].x
                dy = self.balls[i].y - self.balls[j].y
                dist = np.sqrt(dx * dx + dy * dy)
                if dist < 0.1:  # Проверка на столкновение
                    # Отражение шариков
                    self.balls[i].vx, self.balls[j].vx = self.balls[j].vx, self.balls[i].vx
                    self.balls[i].vy, self.balls[j].vy = self.balls[j].vy, self.balls[i].vy

        self.ax.clear()
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 1)
        self.ax.scatter([b.x for b in self.balls], [b.y for b in self.balls])

    def run(self):
        ani = animation.FuncAnimation(self.fig, self.update, frames=100, interval=50, blit=False)
        plt.show()


# Запуск симуляции
sim = Simulation(num_balls=20)
sim.run()

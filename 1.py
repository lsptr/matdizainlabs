import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def draw_spiral(iterations=1000, scale=1.0, angle_step=0.01):
    theta = np.linspace(0, iterations * angle_step, iterations)
    r = theta * scale

    x = r * np.cos(theta)
    y = r * np.sin(theta)

    return x, y


def animate_spiral(scale=1.0, angle_step=0.01):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect('equal')

    def update(frame):
        x, y = draw_spiral(iterations=frame, scale=scale, angle_step=angle_step)
        ax.clear()
        ax.set_xlim(-100, 100)
        ax.set_ylim(-100, 100)
        ax.plot(x[:frame], y[:frame])

    ani = animation.FuncAnimation(fig, update, frames=1000, interval=1)
    plt.show()


animate_spiral(scale=2.0, angle_step=0.02)
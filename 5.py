import pygame
import math
import random
import pygame_gui
from pygame.locals import QUIT

WIDTH, HEIGHT = 800, 600
FPS = 60


def wave_function(x, amplitude, frequency, phase, wave_type="sin"):
    angle = frequency * (x + phase)
    if wave_type == "sin":
        return amplitude * math.sin(angle)
    elif wave_type == "cos":
        return amplitude * math.cos(angle)


def draw_boat(screen, x, y, size, angle):
    boat_surface = pygame.Surface((200 * size, 100 * size), pygame.SRCALPHA)
    boat_surface.fill((0, 0, 0, 0))

    pygame.draw.polygon(boat_surface, (255, 30, 30),
                        [(60 * size, 10 * size), (80 * size, 100 * size), (130 * size, 50 * size)])

    pygame.draw.rect(boat_surface, (139, 69, 19), (40 * size, 90 * size, 100 * size, 40 * size))


    rotated_boat = pygame.transform.rotate(boat_surface, -angle)
    rect = rotated_boat.get_rect(center=(x, y))
    screen.blit(rotated_boat, rect.topleft)


    rotated_boat = pygame.transform.rotate(boat_surface, -angle)
    rect = rotated_boat.get_rect(center=(x, y))
    screen.blit(rotated_boat, rect.topleft)


def animate_boat():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Кораблик на волне")
    clock = pygame.time.Clock()

    manager = pygame_gui.UIManager((WIDTH, HEIGHT))
    slider = pygame_gui.elements.UIHorizontalSlider(
        relative_rect=pygame.Rect(10, HEIGHT - 50, WIDTH - 20, 30),
        start_value=1.0,
        value_range=(0.5, 2.0),
        manager=manager
    )

    wave_type = random.choice(["sin", "cos"])
    amplitude = random.randint(50, 150)
    frequency = random.uniform(0.005, 0.02)
    phase = 0

    tilt_reduction = 1

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            manager.process_events(event)

        manager.update(clock.get_time())
        size = slider.get_current_value()

        screen.fill((135, 206, 235))

        wave_points = []
        for i in range(WIDTH):
            wave_y = HEIGHT // 2 + wave_function(i, amplitude, frequency, phase, wave_type)
            wave_points.append((i, wave_y))

        wave_points.append((WIDTH, HEIGHT))
        wave_points.append((0, HEIGHT))
        pygame.draw.polygon(screen, (0, 30, 148), wave_points)

        center_x = WIDTH // 2
        center_y = HEIGHT // 2 + wave_function(center_x, amplitude, frequency, phase, wave_type)
        angle = tilt_reduction * math.degrees(
            math.atan(frequency * amplitude * math.cos(frequency * (center_x + phase))))

        draw_boat(screen, center_x, center_y, size, angle)

        manager.draw_ui(screen)
        pygame.display.flip()
        clock.tick(FPS)

        phase -= 5

    pygame.quit()


if __name__ == "__main__":
    animate_boat()
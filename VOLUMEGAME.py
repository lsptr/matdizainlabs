import random
import win32con
import win32api
import subprocess
from sound import Sound
import win32com.client
import pygame
import sys

# Import mixer module for sound playback
import pygame.mixer

# Initialize Pygame
pygame.init()
Sound.volume_set(30)

# Set up screen
width = 640
height = 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('VOLUMEGAME')


class BallPlus(pygame.Rect):
    def __init__(self):
        super().__init__(width // random.randint(1, 10), height // random.randint(1, 10), 30, 30)
        self.speed_x = 4
        self.speed_y = 4

    def draw_plus(self, surface, color=(255, 255, 255)):
        pygame.draw.line(surface, color, (self.centerx - 8, self.centery), (self.centerx + 8, self.centery), 3)
        pygame.draw.line(surface, color, (self.centerx, self.centery - 8), (self.centerx, self.centery + 8),
                         3)


class BallMinus(pygame.Rect):
    def __init__(self):
        super().__init__(width // random.randint(1, 10), height // random.randint(1, 10), 30, 30)
        self.speed_x = 3
        self.speed_y = 3

    def draw_minus(self, surface, color=(255, 255, 255)):
        pygame.draw.line(surface, color, (self.centerx - 8, self.centery), (self.centerx + 8, self.centery), 3)


class Paddle(pygame.Rect):
    def __init__(self):
        super().__init__(width // 2, height - 40, 100, 20)


# Create objects and clock
ball_plus = BallPlus()
ball_minus = BallMinus()
paddle = Paddle()
clock = pygame.time.Clock()

# Initialize mixer module
pygame.mixer.init()


# Function to increase volume
def increase_volume():
    cur = Sound.current_volume()
    Sound.volume_set(cur + 5)

def decrease_volume():
    cur = Sound.current_volume()
    Sound.volume_set(cur - 3)



# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    paddle.centerx = min(width, max(0, paddle.centerx + (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 10))

    ball_plus.x += ball_plus.speed_x
    ball_plus.y += ball_plus.speed_y

    ball_minus.x += ball_minus.speed_x
    ball_minus.y += ball_minus.speed_y

    if ball_plus.top < 0 or ball_plus.bottom > height:
        ball_plus.speed_y *= -1
    if ball_minus.top < 0 or ball_minus.bottom > height:
        ball_minus.speed_y *= -1
    if ball_plus.left < 0 or ball_plus.right > width:
        ball_plus.speed_x *= -1
    if ball_minus.left < 0 or ball_minus.right > width:
        ball_minus.speed_x *= -1

    if ball_plus.colliderect(paddle):
        ball_plus.speed_y *= -1
        increase_volume()  # Increase volume
        print("volume plus")

        # Play sound effect
        hit_sound = pygame.mixer.Sound("hit.wav")  # Replace with your sound file
        hit_sound.play()

    if ball_minus.colliderect(paddle):
        ball_minus.speed_y *= -1
        decrease_volume()  # Decrease volume
        print("volume minus")

        # Play sound effect
        hit_sound = pygame.mixer.Sound("hit.wav")  # Replace with your sound file
        hit_sound.play()

    if ball_plus.bottom > height:
        running = False
    if ball_minus.bottom > height:
        ball_minus = False

    screen.fill((150, 255, 150))
    pygame.draw.rect(screen, (230, 110, 0), paddle)
    pygame.draw.ellipse(screen, (43, 134, 19), ball_plus)
    ball_plus.draw_plus(screen)
    pygame.draw.ellipse(screen, (235, 90, 90), ball_minus)
    ball_minus.draw_minus(screen)

    pygame.display.flip()
    clock.tick(60)

print("Game over!")
pygame.quit()
sys.exit()

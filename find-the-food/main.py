import pygame
import math
import random
from bug import Bug

# Example usage:
pygame.init()
screen = pygame.display.set_mode((800, 600))
screen_width, screen_height = screen.get_size()
clock = pygame.time.Clock()

bug = Bug(100, 100, screen, screen_width, screen_height)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    randChange = random.randint(-100, 100) / 100
    bug.move(randChange, 1 - abs(randChange))  # Rotate slightly right and increase speed

    screen.fill((0, 0, 0))  # Fill the screen with white
    bug.draw()
    pygame.display.flip()
    clock.tick(60)  # Limit to 60 frames per second

pygame.quit()
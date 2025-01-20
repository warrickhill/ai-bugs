import pygame
import math
import random
from bug import BugWithBrain

# Example usage:
pygame.init()
screen = pygame.display.set_mode((800, 600))
screen_width, screen_height = screen.get_size()
clock = pygame.time.Clock()

# Create a BugWithBrain instance
brain_bug = BugWithBrain(100, 100, screen, screen_width, screen_height)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get action from the bug's brain
    rotation_change, speed_adjust = brain_bug.get_action([brain_bug.x, brain_bug.y])
    brain_bug.move(rotation_change, speed_adjust)

    screen.fill((0, 0, 0))  # Fill the screen with black
    brain_bug.draw()

    # Get FPS
    fps = str(int(clock.get_fps()))

    # Display FPS on the screen
    font = pygame.font.Font(None, 24)
    fps_text = font.render(fps, True, (255, 255, 255))
    text_rect = fps_text.get_rect(topleft=(10, 10))
    screen.blit(fps_text, text_rect)

    pygame.display.flip()
    clock.tick(60)  # Limit to 60 frames per second

pygame.quit()
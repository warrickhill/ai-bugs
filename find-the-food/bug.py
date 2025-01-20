import pygame
import math

class Bug:
    def __init__(self, x, y, screen, screen_width, screen_height):
        self.x = x
        self.y = y
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.width = 30
        self.height = 20
        self.color = (255, 0, 0)  # Red
        self.eye_color = (255, 255, 255)  # Black
        self.speed = 0  # Initial speed is 0
        self.angle = 0  # Initial angle is 0 degrees
        self.max_speed = 5
        self.max_speed_adjust = 2
        self.max_turn = math.radians(100)  # Maximum turn angle

        # Create the bug shape as a surface
        self.bug_shape = pygame.Surface((self.width, self.height))
        pygame.draw.ellipse(self.bug_shape, self.color, (0, 0, self.width, self.height)) 
        ## Add eyes to the bug shape
        eye_radius = 3
        eye_offset_x = self.width // 4  # Adjust offset for more forward eyes
        eye_offset_y = self.height // 4 # Keep eyes centered vertically
        pygame.draw.circle(self.bug_shape, self.eye_color, (self.width - eye_offset_x, eye_offset_y), eye_radius)
        pygame.draw.circle(self.bug_shape, self.eye_color, (self.width - eye_offset_x, self.height - eye_offset_y), eye_radius)

    def draw(self):
        # Calculate the center of the bug
        center_x = self.x + self.width // 2
        center_y = self.y + self.height // 2

        # Create a rotated surface
        rotated_bug = pygame.transform.rotate(self.bug_shape, math.degrees(-self.angle))

        # Calculate the new position of the rotated bug
        rotated_rect = rotated_bug.get_rect(center=(center_x, center_y))

        # Blit the rotated bug onto the screen
        self.screen.blit(rotated_bug, rotated_rect)

        # Print the current angle (optional)
        font = pygame.font.Font(None, 24)
        text = f"Angle: {math.degrees(self.angle):.2f}"
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(topleft=(10, 10))
        self.screen.blit(text_surface, text_rect)
        
    def move(self, rotation_change, speed_adjust):
        # Clamp rotation change within -1 to 1
        rotation_change = max(-1, min(1, rotation_change)) 
        # Clamp speed adjust within -1 to 1
        speed_adjust = max(-1, min(1, speed_adjust)) 

        # Calculate the change in angle
        angle_change = rotation_change * self.max_turn 
        self.angle += math.radians(angle_change)

        # Calculate the change in speed
        self.speed += speed_adjust * self.max_speed_adjust
        self.speed = max(0, min(self.speed, self.max_speed))  # Clamp speed within 0 to max_speed

        # Calculate the movement in x and y directions
        dx = self.speed * math.cos(self.angle)
        dy = self.speed * math.sin(self.angle)

        # Check for wall collisions and bounce
        if self.x + dx < 0 or self.x + dx + self.width > self.screen_width:
            self.angle = math.pi - self.angle  # Invert x-axis component
        if self.y + dy < 0 or self.y + dy + self.height > self.screen_height:
            self.angle = -self.angle  # Invert y-axis component

        # Update position
        self.x += dx
        self.y += dy
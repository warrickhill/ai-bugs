import pygame 
  
pygame.init() 
  
# CREATING CANVAS 
canvas = pygame.display.set_mode((1000, 800)) 
  
# TITLE OF CANVAS 
pygame.display.set_caption("Bugs Ai - Find the food") 
exit = False
  
while not exit: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
    pygame.display.update() 
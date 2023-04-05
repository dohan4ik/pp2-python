import pygame
import random
pygame.init()
monitor = pygame.display.set_mode((100, 50))
check = True
while check:
    monitor.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    pygame.display.update()
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            pygame.image.save(monitor, "activitytask4week9.png")
            check = False 
            pygame.quit()

import pygame
pygame.init()
pygame.display.set_caption("WEEK 9 ACTIVITY TASK")
monitor = pygame.display.set_mode((800, 600))
check = True
while check:
    monitor.fill((7,23, 249))
    pygame.display.update()
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            check = False 
            pygame.quit()
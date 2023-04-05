import pygame
pygame.init()
pygame.display.set_caption("WEEK 9 TASK 2")
monitor = pygame.display.set_mode((800, 400))
check = True 
clock = pygame.time.Clock()
x = 0
y = 0
z = 10
FPS = 30
pos = (x,y,z,z)
color = (0, 255, 0)
while check:
    clock.tick(FPS)
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            check = False 
    keys = pygame.key.get_pressed()
    if keys[]
    monitor.fill((0, 0, 0))
    pygame.draw.rect(monitor, color, pos)
    pygame.display.update()

pygame.quit()
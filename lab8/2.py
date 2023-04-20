import pygame, sys
def car():
    car1 = pygame.image.load('lab8/image/mycar.png')
    rect = car1.get.rect()
    monitor_rect = monitor.get_rect()
    rect_centerx = monitor_rect.centerx
    rect_bottom = monitor_rect.bottom
    monitor.blit(car1, rect)
pygame.init()
monitor = pygame.display.set_mode((700, 500))
pygame.display.set_caption("racer by me")
check = True 
while check:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            check = False
    car()
    monitor.fill((60, 60, 60))
    pygame.display.update()
          
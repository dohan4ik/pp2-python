import pygame
pygame.init()
monitor = pygame.display.set_mode((510, 510))
pygame.display.set_caption("LAB 7 TASK 3")
clock = pygame.time.Clock()
x = 25
y = 25
size = 50
Fps = 30
pos = (x, y , size, size)
check = True
while check:
    clock.tick(Fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            check = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if y - 20 > 20:
            y -= 20
    if keys[pygame.K_DOWN]:
        if y + 20 < 490:
            y += 20
    if keys[pygame.K_LEFT]:
        if x - 20 > 20:
            x -= 20
    if keys[pygame.K_RIGHT]:
        if x + 20 < 490:
            x += 20
    monitor.fill((255, 255, 255))
    pygame.draw.circle(monitor, (155, 70, 255), (x, y), 25)
    pygame.display.update()


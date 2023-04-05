import pygame
pygame.init()
monitor = pygame.display.set_mode((400, 400))
monitor.fill((86, 86, 86))
font = pygame.font.Font(None, 30) #шрифт
check = True
while check:
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            check = False
            pygame.quit()
        if action.type == pygame.KEYDOWN:
            key_name = pygame.key.name(action.key)
            text_surface = font.render(key_name, True, (255, 255, 255))
            print(key_name)
            monitor.blit(text_surface, (200, 180))
            pygame.display.update()
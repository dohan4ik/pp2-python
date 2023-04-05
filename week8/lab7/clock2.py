import pygame
from datetime import datetime
import math

WIDTH = 1200
HEIGHT = 800
H_WIDTH = 600
H_HEIGHT = 400
RADIUS = H_HEIGHT - 50
radius_list = {'sec': RADIUS -10, 'min': RADIUS - 55, 'hour': RADIUS - 100}

pygame.init()
monitor = pygame.display.set_mode((WIDTH, HEIGHT))
check = True
clock = pygame.time.Clock()
font = pygame.font.SysFont('Verdana', 60)
clock_h = dict(zip(range(12), range(0, 360 , 30)))
clock_m = dict(zip(range(60), range(0,360, 6)))

def get_clock_pos(clock_dict, clock_hand, key):
    x = H_WIDTH + radius_list[key] * math.cos(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    y = H_HEIGHT + radius_list[key] * math.sin(math.radians(clock_dict[clock_hand] - math.pi) / 2)
    return x, y

while check:
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            check = False 
            pygame.quit()
    monitor.fill(pygame.Color('black'))
    time = datetime.now()
    hour = time.hour % 12
    minute = time.minute
    second = time.second
    pygame.draw.circle(monitor, pygame.Color('darkslategray'), (H_WIDTH, H_HEIGHT), RADIUS)
    pygame.draw.line(monitor, pygame.Color('orange'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock_h, hour, 'hour'), 15)
    pygame.draw.line(monitor, pygame.Color('green'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock_m, minute, 'min'), 7)
    pygame.draw.line(monitor, pygame.Color('magenta'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock_m, second, 'sec'), 4)
    pygame.draw.circle(monitor, pygame.Color('white'),  (H_WIDTH, H_HEIGHT), 8)
    time_render = font.render(f'{time:%H:%M:%S}', True, pygame.Color('forestgreen'), pygame.Color('orange'))
    monitor.blit(time_render, (0, 0))
    pygame.display.flip()
    pygame.display.update()
    clock.tick(20)
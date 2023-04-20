import pygame
#from datetime 
import datetime
import math

pygame.init()
screen = pygame.display.set_mode((835, 837))

RADIUS = 837 // 2 - 100
radius_list = {'sec': RADIUS - 10, 'min': RADIUS - 55, 'hour': RADIUS - 100}

clock = pygame.time.Clock()
Body = pygame.image.load('images/main-clock.png')
Body = pygame.transform.scale(Body, (835, 837))

Right = pygame.image.load('images/Right.png')
Right = pygame.transform.scale(Right, (65, 837))

Left = pygame.image.load('images/Left.png')
Left = pygame.transform.scale(Left, (99, 837))
                 
# def get_clock_pos(clock_dict, clock_hand, key):
#     x = 835 // 2 + radius_list[key] * math.cos(math.radians(clock_dict[clock_hand]) - math.pi / 2)
#     y = 837 // 2 + radius_list[key] * math.sin(math.radians(clock_dict[clock_hand]) - math.pi / 2)
#     return x, y

# clock60 = dict(zip(range(60), range(0, 360, 6)))  # for hours, minutes and seconds

done = False
angle = 0
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        #t = datetime.now()
        #hour, minute, second = ((t.hour % 12) * 5 + t.minute // 12) % 60, t.minute, t.second

        now = datetime.datetime.now()
        second = int(now.second)
        minute = int(now.minute)
        
        
        angle1 = angle - second * 6 
        angle2 = angle - minute * 6
        # angle3 = angle - hour * 6

        screen.blit(Body, (0, 0))
        rotated_Right = pygame.transform.rotate(Right, angle2)
        rotated_Left = pygame.transform.rotate(Left, angle1)

        new_rect = rotated_Right.get_rect(center = Body.get_rect().center)
        new_rect1 = rotated_Left.get_rect(center = Body.get_rect().center)

        screen.blit(rotated_Right, new_rect)
        screen.blit(rotated_Left, new_rect1)

        # pygame.draw.line(screen, pygame.Color('black'), (835 // 2, 837 // 2), get_clock_pos(clock60, second, 'sec'))

        pygame.display.flip()
        clock.tick(60)
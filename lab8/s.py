import pygame, sys, random     #sys  -  дает доступ системным функциям
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(7, 10), Vector2(6, 10), Vector2(5, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:    
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(monitor, (183, 111, 122), block_rect)
    
    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block =True

class FRUIT:
    def __init__(self):
        self.randomize()
        # создаем позицию х и у
        # нарисовать квадрат

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        pygame.draw.rect(monitor,(126, 166, 114), fruit_rect)
        # создать и нарисовать прямоугольник 

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = pygame.math.Vector2(self.x, self.y)


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
    
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
    
    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
    can = 0
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            can += 1
            self.snake.add_block()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x <= cell_number or not 0 <= self.snake.body[0].y <= cell_number:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()
    

pygame.init()
cell_size = 30
cell_number = 20
pygame.display.set_caption("S N A K E")  
monitor = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
clock = pygame.time.Clock()
# fruit = FRUIT()
# snake = SNAKE()
main_game = MAIN()
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)
# test_surface = pygame.Surface((100, 200))
# test_surface.fill((0, 0, 255))
# test_rect = test_surface.get_rect(center = (200, 250))
# test_rect = pygame.Rect(100, 200, 100, 100)
#x_pos = 100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            # snake.move_snake()
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, +1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(+1, 0)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
    monitor.fill((70, 215, 70))
    # fruit.draw_fruit()
    # snake.draw_snake()
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
    # pygame.draw.rect(monitor, pygame.Color('red'), test_rect)
    # x_pos += 1
    # monitor.blit(test_surface, test_rect)
    # test_rect.right += 1 
    #monitor.blit(test_surface, (200, 250))
    
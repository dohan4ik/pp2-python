import pygame
import time
import random

# инициализация
pygame.init()

# colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (50, 153, 213)


dis_width = 600
dis_height = 400
fps = 10
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake')
 
clock = pygame.time.Clock()
 
snake_block = 10
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# функция вывода текста счёта и уровня
def Your_score(score, levels):
    value = score_font.render("Your Score: " + str(score), True, black)
    dis.blit(value, [0, 0])
    level_score = score_font.render("Level: " + str(levels), True, black)
    dis.blit(level_score, [450, 0])

# функция отрисовки змеи
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

# функция вывода текста на экран
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# главный цикл игры
def gameLoop():
    game_over = False
    game_close = False

    # начальное положение змеи
    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    # начальные координаты стенок
    walls = [[20, 30], [300, 100], [450, 250]]

    # уровень игры
    level = 1

    while not game_over:

        # цикл, который выполняется при окончании игры
        while game_close == True:
            dis.fill(white)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1, level)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # главный цикл
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
            
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        levels = 0
        
        if (Length_of_snake - 1) >= 3 and (Length_of_snake - 1) < 6:
            levels = 1
            pygame.draw.rect(dis, blue, [100, 100, snake_block, snake_block])
            pygame.draw.rect(dis, blue, [350, 350, snake_block, snake_block])
            pygame.draw.rect(dis, blue, [400, 200, snake_block, snake_block])
        if (Length_of_snake - 1) >= 6 and (Length_of_snake - 1) < 9:
            levels = 2
            pygame.draw.rect(dis, blue, [100, 100, snake_block, snake_block])
            pygame.draw.rect(dis, blue, [350, 350, snake_block, snake_block])
            pygame.draw.rect(dis, blue, [400, 200, snake_block, snake_block])
            pygame.draw.rect(dis, blue, [500, 200, snake_block, snake_block])
            pygame.draw.rect(dis, blue, [450, 300, snake_block, snake_block])
            pygame.draw.rect(dis, blue, [200, 400, snake_block, snake_block])
        if (Length_of_snake - 1) >= 9 and (Length_of_snake - 1) < 12:
            levels = 3
        if (Length_of_snake - 1) >= 12 and (Length_of_snake - 1) < 15:
            levels = 4
        if levels == 1:
            for x in snake_List:
                if x == [100, 100] or x == [350, 350] or x == [400, 200]:
                    game_over = True
                    game_close = True
        if levels == 2:
            for x in snake_List:
                if x == [100, 100] or x == [350, 350] or x == [400, 200] or x == [500, 200] or x == [450, 300] or x == [200, 400]:
                    game_over = True
                    game_close = True
        Your_score(Length_of_snake - 1, levels)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
        if levels >= 1:
            clock.tick(fps * int(levels))
        else:
            clock.tick(fps)
 
    pygame.quit()
    quit()
 
 
gameLoop()
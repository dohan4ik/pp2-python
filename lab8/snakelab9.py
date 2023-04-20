import pygame
import time
import random

pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (50, 153, 213)

# Define display dimensions and frames per second
dis_width = 600
dis_height = 400
fps = 10

# Set up the display window
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake')

# Set up the clock for the game loop
clock = pygame.time.Clock()

# Set the size of each block in the snake
snake_block = 10

# Define fonts to use for score and level display
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to display the player's score and current level
def Your_score(score, levels):
    value = score_font.render("Your Score: " + str(score), True, black)
    dis.blit(value, [0, 0])
    level_score = score_font.render("Level: " + str(levels), True, black)
    dis.blit(level_score, [450, 0])
# Function to draw the snake

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

# Function to display a message to the player
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# Main game loop
def gameLoop():
    # Set game over and game close variables to false to start
    game_over = False
    game_close = False

    # Set initial position of the snake
    x1 = dis_width / 2
    y1 = dis_height / 2

    # Set initial direction of movement to 0 (not moving)
    x1_change = 0
    y1_change = 0

    # Create an empty list to store the positions of the snake's body segments
    snake_List = []

    # Set the initial length of the snake to 1
    Length_of_snake = 1

    # Generate the first food block at a random position on the screen
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    # Run the game until the player quits or loses
    while not game_over:

        # If the player has lost, display a message and allow them to play again or quit
        while game_close == True:
            dis.fill()
            message("You Lost! Press C-Play Again or Q-Quit", green)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Check for events (e.g. keyboard input, window closing)
        #главный цикл
        for event in pygame.event.get():
            #выход через верхнию кнопку
            if event.type == pygame.QUIT:
                game_over = True
            #зажимаие клавы
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
            random_number = random.randint(1, 3)
            Length_of_snake += random_number
        if levels >= 1:
            clock.tick(fps * int(levels))
        else:
            clock.tick(fps)
 
    pygame.quit()
    quit()
 
 
gameLoop()
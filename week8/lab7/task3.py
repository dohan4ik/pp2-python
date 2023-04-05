import pygame

# initialize pygame
pygame.init()

# set screen size
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# set circle position and size
circle_radius = 25
circle_x = screen_width // 2
circle_y = screen_height // 2

# set colors
white = (255, 255, 255)
red = (255, 0, 0)

# draw circle
def draw_circle():
    pygame.draw.circle(screen, red, (circle_x, circle_y), circle_radius)

# main game loop
running = True
while running:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if circle_y - 20 >= circle_radius:
                    circle_y -= 20
            elif event.key == pygame.K_DOWN:
                if circle_y + 20 <= screen_height - circle_radius:
                    circle_y += 20
            elif event.key == pygame.K_LEFT:
                if circle_x - 20 >= circle_radius:
                    circle_x -= 20
            elif event.key == pygame.K_RIGHT:
                if circle_x + 20 <= screen_width - circle_radius:
                    circle_x += 20
    
    # fill background with white color
    screen.fill(white)

    # draw circle
    draw_circle()

    # update screen
    pygame.display.flip()

# quit pygame
pygame.quit()

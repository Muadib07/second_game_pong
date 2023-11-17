import sys
import pygame


# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 580
screen_height = 680
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# game Rectangles
ball = pygame.Rect((screen_width/2-15, screen_height/2 - 15, 30, 30))
player = pygame.Rect((screen_width/2+220, screen_height/2 - 70, 10, 140))
opponent = pygame.Rect((10, screen_height/2 - 70, 10, 140))



# game color options
bg_color = pygame.Color('gray12')
light_grey = (200, 200, 200)

# ball speed setings
ball_speed_x = 5
ball_speed_y = 5

while True:
    # handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Use pygame.QUIT to check for quit event
            pygame.quit()
            sys.exit()

    # Game logic and drawing would go here

    # Ball behavior
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1

    # player collision
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

    # Visual
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))
    # upadting the window
    pygame.display.flip()
    clock.tick(60)
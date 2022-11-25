import pygame
from sys import exit
from random import randint

pygame.init()

# screen size
WIDTH = 800
HEIGHT = 400

# variables
ball_x = 400
ball_y = 200
ball_speed_x = 4
ball_speed_y = 2
acceleration = 0.001 * randint(1, 10)
print(acceleration)

player_y = 200
enemy_y = 200
speed = 4


screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()

ball_surf = pygame.Surface((15,15))
ball_surf.fill('White')
ball_rect = ball_surf.get_rect(center = (ball_x, ball_y))

player_surf = pygame.Surface((15,150))
player_surf.fill('White')
player_rect = player_surf.get_rect(center = (70, player_y))


enemy_surf = pygame.Surface((15,150))
enemy_surf.fill('White')
enemy_rect = enemy_surf.get_rect(center = (WIDTH-70, enemy_y))

while True:
    keys = pygame.key.get_pressed()
    # check for exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # check bounce
    if ball_rect.colliderect(player_rect) and ball_speed_x < 0: 
        ball_speed_x = -ball_speed_x
    if ball_rect.colliderect(enemy_rect) and ball_speed_x > 0:
        ball_speed_x = -ball_speed_x

    if ball_rect.top <= 0 and ball_speed_y < 0:
        ball_speed_y = -ball_speed_y
    elif ball_rect.bottom >= HEIGHT and ball_speed_y > 0:
            ball_speed_y = -ball_speed_y

    if ball_rect.left <=0 or ball_rect.right >= WIDTH:
        pygame.quit()
        exit()
    
    # accelerate ball
    if ball_speed_y > 0:
        ball_speed_y += acceleration
    else:
        ball_speed_y -= acceleration
    
    # player ai
    if ball_rect.center[0] >= 400:
        if ball_rect.center[1] > enemy_rect.center[1]:
            if enemy_rect.bottom < HEIGHT:
                enemy_rect.bottom += speed

        if ball_rect.center[1] < enemy_rect.center[1]:
            if enemy_rect.top > 0:
                enemy_rect.top -= speed

    if keys[pygame.K_UP]:
        if player_rect.top > 0:
            player_rect.top -= speed
    elif keys[pygame.K_DOWN]:
        if player_rect.bottom < HEIGHT:
            player_rect.bottom += speed

    # change ball position
    ball_rect.left += ball_speed_x
    ball_rect.bottom += ball_speed_y
    
    # show stuff on screen
    screen.blit(ball_surf, ball_rect)
    screen.blit(player_surf, player_rect)
    screen.blit(enemy_surf, enemy_rect)
    
    # update screen
    pygame.display.update()
    
    # clear screen
    screen.fill('Black')
    clock.tick(60)

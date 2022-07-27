#!/usr/bin/env python
# pygame is computer graphics and sound libraries designed to be used with the Python programming language.
import pygame
import random  # this allows for the creation of random integers through a library
import sys  # this imports the library that will enable the user to quit out of the screen

pygame.init()

# Initializing Variables
width = 800  # initializes width variable of the screen
height = 600  # initializes height variable of the screen
drop_speed = 10
# Defining Colors
red = (236, 3, 252)
blue = (0, 0, 255)
yellow = (255, 255, 0)
background_color = (0, 0, 0)

# Player Information
player_size = 50
player_pos = [width/2, height-2*player_size]

# Enemy Information
enemy_size = 50
enemy_pos = [random.randint(0, width - enemy_size), 0]
enemy_list = [enemy_pos]

screen = pygame.display.set_mode((width, height))

game_over = False

score = 0

clock = pygame.time.Clock()

myFont = pygame.font.SysFont("monospace", 35, )

# defining the level function


def set_lvl(score, drop_speed):
    # if score < 20:
    #drop_speed = 5
    # elif score < 40:
    #drop_speed = 8
    # elif score < 60:
    #drop_speed = 12
    # else:
    #drop_speed = 15
    # return drop_speed
    drop_speed = score/20+3
    return drop_speed

# dropping multiple enemies function


def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) < 10 and delay < 0.3:
        x_pos = random.randint(0, width-enemy_size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])

# draw enemies function


def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(
            screen, blue, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

# updating enemy position function


def update_enemy_pos(enemy_list, score):
    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < height:  # falling script
            enemy_pos[1] += drop_speed  # controls the fall speed for the enemy

        else:
            enemy_list.pop(idx)
            score += 1
    return score

# collision check function


def collision_check(enemy_list, player_pos):
    for enemy_pos in enemy_list:
        if detect_collsion(enemy_pos, player_pos):
            return True
    return False

# collision detection function


def detect_collsion(player_pos, enemy_pos):
    # player
    p_x = player_pos[0]
    p_y = player_pos[1]
    # enemy
    e_x = enemy_pos[0]
    e_y = enemy_pos[1]

    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (p_x < enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (p_y < enemy_size)):
            return True
    return False


while not game_over:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if player_pos[0] == 800 and 0:
            game_over = True

        if event.type == pygame.KEYDOWN:  # this section of code is used to manipulate the player in the x_pos with the future mod of y_pos
            x = player_pos[0]
            y = player_pos[1]
            if event.key == pygame.K_LEFT:
                x -= player_size  # the player moves +/- the distance of player_size

            elif event.key == pygame.K_RIGHT:
                x += player_size

            player_pos = [x, y]

            if x > width or x < 0 or x > 800:
                game_over = True

    # this line of code fills in the space so the player doesn't track across the screen like painting
    screen.fill(background_color)

    drop_enemies(enemy_list)
    score = update_enemy_pos(enemy_list, score)
    drop_speed = set_lvl(score, drop_speed)

    text = "score" + str(score)
    label = myFont.render(text, 1, yellow)
    screen.blit(label, (width-200, height-40))

    if collision_check(enemy_list, player_pos):
        game_over = True
        break

    # rect_enenmy enemy_pos[1] has to change for falling, refer to function above
    draw_enemies(enemy_list)

    # code creates rectangle: rect(surface, color, rect) -> rect_player
    pygame.draw.rect(
        screen, red, (player_pos[0], player_pos[1], player_size, player_size))

    clock.tick(30)

    pygame.display.update()  # code refreshes and enables the rect to appear on the screen

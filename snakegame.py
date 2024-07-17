import pygame
import random
from pygame.locals import *

pygame.init()

snake_color = (242, 255, 0)  # yellow
food_color = (255, 0, 0)  # red
bg_color = (51, 255, 0)  # green
score_color = (255, 255, 255)  # white

win_width = 600
win_height = 400

window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Snake Game")

snake_block = 10
snake_speed = 15

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("calibri", 26)
score_font = pygame.font.SysFont("comicsansms", 30)

highest_score = 0

def user_score(score, highest_score):
    score_text = score_font.render(f"Score: {score}", True, score_color)
    highest_score_text = score_font.render(f"Highest Score: {highest_score}", True, score_color)
    window.blit(score_text, [0, 0])
    window.blit(highest_score_text, [0, 30])

def game_snake(snake_block, snake_length_list):
    for x in snake_length_list:
        pygame.draw.rect(window, snake_color, [x[0], x[1], snake_block, snake_block])

def message(msg):
    msg = font_style.render(msg, True, food_color)
    window.blit(msg, [win_width / 6, win_height / 3])

def game_loop():
    global highest_score
    gameOver = False
    gameClose = False

    x1 = win_width / 2
    y1 = win_height / 2

    x1_change = 0
    y1_change = 0

    snake_length_list = []
    snake_length = 1    

    foodx = round(random.randrange(0, win_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, win_height - snake_block) / 10.0) * 10.0

    while not gameOver:
        while gameClose:
            window.fill(bg_color)
            message("You Lost! Press Q-Quit or P-Play Again")
            user_score(snake_length - 1, highest_score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
                    gameClose = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        gameClose = False
                    if event.key == pygame.K_p:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == K_a and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == K_d and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == K_w and y1_change == 0:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == K_s and y1_change == 0:
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= win_width or x1 < 0 or y1 >= win_height or y1 < 0:
            gameClose = True

        x1 += x1_change
        y1 += y1_change
        window.fill(bg_color)
        pygame.draw.rect(window, food_color, [foodx, foody, snake_block, snake_block])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_length_list.append(snake_head)

        if len(snake_length_list) > snake_length:
            del snake_length_list[0]

        for x in snake_length_list[:-1]:
            if x == snake_head:
                gameClose = True

        game_snake(snake_block, snake_length_list)
        user_score(snake_length - 1, highest_score)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, win_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, win_height - snake_block) / 10.0) * 10.0
            snake_length += 1

            if snake_length - 1 > highest_score:
                highest_score = snake_length - 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()

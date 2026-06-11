# Snake Game using Python and Pygame
# First install pygame:
# pip install pygame

import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH = 600
HEIGHT = 400

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock and FPS
clock = pygame.time.Clock()
FPS = 10

# Snake settings
snake_block = 20
snake_speed = 20

# Font
font = pygame.font.SysFont("arial", 25)

def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], snake_block, snake_block])

def message(text, color, y_offset=0):
    msg = font.render(text, True, color)
    screen.blit(msg, [WIDTH / 6, HEIGHT / 3 + y_offset])

def game_loop():
    game_over = False
    game_close = False

    # Snake starting position
    x = WIDTH // 2
    y = HEIGHT // 2

    x_change = 0
    y_change = 0

    snake_list = []
    snake_length = 1

    # Food position
    food_x = round(random.randrange(0, WIDTH - snake_block) / 20.0) * 20
    food_y = round(random.randrange(0, HEIGHT - snake_block) / 20.0) * 20

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            message("You Lost!", RED)
            message("Press Q to Quit or C to Play Again", WHITE, 40)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False

                    if event.key == pygame.K_c:
                        game_loop()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_speed
                    y_change = 0

                elif event.key == pygame.K_RIGHT:
                    x_change = snake_speed
                    y_change = 0

                elif event.key == pygame.K_UP:
                    y_change = -snake_speed
                    x_change = 0

                elif event.key == pygame.K_DOWN:
                    y_change = snake_speed
                    x_change = 0

        # Wall collision
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        # Move snake
        x += x_change
        y += y_change

        # Draw background
        screen.fill(BLACK)

        # Draw food
        pygame.draw.rect(screen, RED, [food_x, food_y, snake_block, snake_block])

        # Snake body
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)

        snake_list.append(snake_head)

        # Remove extra blocks
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Self collision
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        # Draw snake
        draw_snake(snake_list)

        # Score
        score = font.render("Score: " + str(snake_length - 1), True, WHITE)
        screen.blit(score, [10, 10])

        pygame.display.update()

        # Food collision
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - snake_block) / 20.0) * 20
            food_y = round(random.randrange(0, HEIGHT - snake_block) / 20.0) * 20
            snake_length += 1

        clock.tick(FPS)

    pygame.quit()
    quit()

# Start game
game_loop()
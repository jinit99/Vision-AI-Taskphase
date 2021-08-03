import pygame
import time
import random
# initialize the game

pygame.init()

# setting colours

white = (255, 255, 255)
red = (213, 50, 80)
black = (40, 40, 40)
blue = (50, 153, 213)
green = (0, 255, 0)
yellow = (255, 255, 102)
# initialising the game window

width, height = 800, 600

dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game by Jinit')
# initializing the clock to track time

clock = pygame.time.Clock()

# setting the speed of the snake
snake_block = 10
snake_speed = 15
# setting the font
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# function to print score

# render is used to write thext on the screen surface


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

# function for defining the snake size and its colour


def game_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, red, [x[0], x[1], snake_block, snake_block])

# for defining the message and its colour


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [width / 6, height / 3])


def run_loop():
    game_over = False
    game_close = False
# defining various parameters
    x_1 = width / 2
    y_1 = height / 2

    x_1_change = 0
    y_1_change = 0

    snake_List = []
    Length_of_snake = 1
# giving a random location to the food or the target
    target_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    target_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:  # if game is not over

        while game_close == True:
            dis.fill(black)
            # message to be printed on losing
            message("You Lost! Press 1 to Play Again or 2 to Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()  # to update the changes

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:  # keydown means when any key is pressed
                    if event.key == pygame.K_2:  # here K_1 means the number key 1
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_1:
                        run_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # various events for the movement of snake and to quit
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_1_change = -snake_block
                    y_1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_1_change = snake_block
                    y_1_change = 0
                elif event.key == pygame.K_UP:
                    y_1_change = -snake_block
                    x_1_change = 0
                elif event.key == pygame.K_DOWN:
                    y_1_change = snake_block
                    x_1_change = 0

        if x_1 >= width or x_1 < 0 or y_1 >= height or y_1 < 0:  # setting boundary limits
            game_close = True
        x_1 += x_1_change
        y_1 += y_1_change
        dis.fill(black)
        pygame.draw.rect(
            dis, green, [target_x, target_y, snake_block, snake_block])  # drawing the snake block
        snake_Head = []
        snake_Head.append(x_1)
        snake_Head.append(y_1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:  # when snake eats itself
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        game_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x_1 == target_x and y_1 == target_y:  # code to increase the length of snake after getting the target
            target_x = round(random.randrange(
                0, width - snake_block) / 10.0) * 10.0
            target_y = round(random.randrange(
                0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

# to quit
    pygame.quit()
    quit()


run_loop()

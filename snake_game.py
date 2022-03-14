import pygame
import sys
import random
import time

BACKGROUND = (235, 205, 30)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 600, 600
BOX_SIZE = 30

GAME_WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game by Giedrius')

#flag for the game loop.
game_running = True

pygame.init()
FONT = pygame.font.SysFont(None, 40)


#names of classes and methods below are self explanatory of their intended purpose.

class Apple:
    def __init__(self):
        self.apple_image = pygame.image.load("Images/apple.jpg")
        self.apple_x = random.randint(1, 19) * BOX_SIZE
        self.apple_y = random.randint(1, 19) * BOX_SIZE
        self.apple_position = (self.apple_x, self.apple_y)

    def randomize_apple(self):
        self.apple_x = random.randint(1, 19) * BOX_SIZE
        self.apple_y = random.randint(1, 19) * BOX_SIZE
        self.apple_position = (self.apple_x, self.apple_y)

    def draw_apple(self):
        GAME_WINDOW.blit(self.apple_image, self.apple_position)


class Snake:
    def __init__(self):
        self.snake_image = pygame.image.load("Images/snake.jpg")
        self.snake_x = 90
        self.snake_y = 90
        self.snake_list = [[self.snake_x, self.snake_y]]
        self.direction = "right"

    def move_snake(self):
        if self.direction == "up":
            self.snake_y -= BOX_SIZE
        if self.direction == "right":
            self.snake_x += BOX_SIZE
        if self.direction == "down":
            self.snake_y += BOX_SIZE
        if self.direction == "left":
            self.snake_x -= BOX_SIZE
        self.snake_list.insert(0, [self.snake_x, self.snake_y])
        self.snake_list.pop(-1)

    def draw_snake(self):
        for part in self.snake_list:
            GAME_WINDOW.blit(self.snake_image, (part[0], part[1]))


def check_for_snake_eating_apple(snake, apple):
    if snake.snake_list[0][0] == apple.apple_x and snake.snake_list[0][1] == apple.apple_y:
        apple.randomize_apple()
        snake.snake_list.insert(0, snake.snake_list[0])


def check_for_collision_with_border(snake):
    global game_running
    if snake.snake_list[0][0] < 0 or snake.snake_list[0][0] == WIDTH \
            or snake.snake_list[0][1] < 0 or snake.snake_list[0][1] == HEIGHT:
        game_running = False


def check_for_collision_with_self(snake):
    global game_running
    for part in snake.snake_list[3:]:
        if part[0] == snake.snake_list[0][0] and part[1] == snake.snake_list[0][1]:
            game_running = False


def draw_game(snake, apple):
    GAME_WINDOW.fill(BACKGROUND)
    apple.draw_apple()
    snake.draw_snake()
    check_for_snake_eating_apple(snake, apple)
    check_for_collision_with_border(snake)
    check_for_collision_with_self(snake)
    snake.move_snake()
    pygame.display.update()


def control_snake(snake, key):
    if key == pygame.K_UP:
        snake.direction = "up"
    if key == pygame.K_RIGHT:
        snake.direction = "right"
    if key == pygame.K_DOWN:
        snake.direction = "down"
    if key == pygame.K_LEFT:
        snake.direction = "left"


def message_to_screen(msg, color):
    text = FONT.render(msg, True, color)
    GAME_WINDOW.blit(text, (200, 260))
    pygame.display.update()


def main():
    snake = Snake()
    apple = Apple()

#game loop. will run while the flag is set to true.
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                control_snake(snake, event.key)
        draw_game(snake, apple)
        time.sleep(0.18)

    GAME_WINDOW.fill(BACKGROUND)
    message_to_screen('GAME OVER', BLACK)
    time.sleep(2)
    pygame.quit()
    sys.exit()


main()
import pygame
import random

pygame.init()
pygame.display.set_caption("Pong Game in Python")
HEIGHT = 800
WIDTH = 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
HEIGHT_PADDLE = 60
WIDTH_PADDLE = 10
VEL_PADDLE = 5
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RADIUS_BALL = 6
COLOUR_BALL = (255, 20, 147)

class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = HEIGHT_PADDLE
        self.width = WIDTH_PADDLE
        self.vel = VEL_PADDLE

    def draw(self,window):
        pygame.draw.rect(window, WHITE, (self.x, self.y, WIDTH_PADDLE, HEIGHT_PADDLE))
    
    def move(self, up, down):
        if (self.y == 0 and up) or (self.y == HEIGHT-HEIGHT_PADDLE and down):
            self.y = self.y
        elif up:
            self.y -= VEL_PADDLE
        elif down:
            self.y += VEL_PADDLE

class Ball:
    def __init__(self, x, y, x_vel, y_vel):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel

    def draw(self, window):
        pygame.draw.circle(window, COLOUR_BALL, (self.x, self.y), RADIUS_BALL)

    def move(self):
        if self.x == 0 or self.x == HEIGHT - RADIUS_BALL:
            self.x_vel *= -1
        if self.y == 0 or self.y == WIDTH - RADIUS_BALL:
            self.y_vel *= -1
        self.x += self.x_vel
        self.y += self.y_vel

def draw(window, paddles, ball):
    window.fill(BLACK)
    for paddle in paddles:
        paddle.draw(window)
    ball.draw(window)
    pygame.display.update()

def main(window):
    clock = pygame.time.Clock()
    run = True

    paddles = [Paddle(50,400), Paddle(750,400)]
    ball = Ball(400,400, random.choice([-2, -1, 1, 2]), random.choice([-2, -1, 1, 2]))
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        keys = pygame.key.get_pressed()
        paddles[0].move(up=keys[pygame.K_UP], down=keys[pygame.K_DOWN])
        paddles[1].move(up=keys[pygame.K_w], down=keys[pygame.K_s])
        ball.move()
        draw(window, paddles, ball)

if __name__ == "__main__":
    main(WINDOW)
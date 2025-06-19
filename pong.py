import pygame
import random
import time

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
green = (0, 255, 0)
blue = (0, 0, 128)

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

    def reset(self, leftPaddle):
        if leftPaddle:
            self.x = 50
            self.y = 400
        else:
            self.x = 750
            self.y = 400


class Ball:
    def __init__(self, x, y, x_vel, y_vel):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel

    def draw(self, window):
        pygame.draw.circle(window, COLOUR_BALL, (self.x, self.y), RADIUS_BALL)

    def move(self):
        if self.y < 0 or self.y > HEIGHT - RADIUS_BALL:
            self.y_vel *= -1
        self.x += self.x_vel
        self.y += self.y_vel

    def bounce(self):
        self.x_vel *= -1.03
    
    def reset(self):
        time.sleep(3)
        self.x = 400
        self.y = 400
        self.x_vel = random.choice([-3, -2, 2, 3])
        self.y_vel = random.choice([-3, -2, 2, 3])

def draw(window, paddles, ball, leftScore, rightScore):
    window.fill(BLACK)
    for paddle in paddles:
        paddle.draw(window)
    ball.draw(window)
    font = pygame.font.Font('freesansbold.ttf', 32)


    Lscore = font.render(str(leftScore), True, green, blue)
    text = Lscore.get_rect()
    text.center = (50, 50)
    WINDOW.blit(Lscore, text)

    Rscore = font.render(str(rightScore), True, green, blue)
    text1 = Rscore.get_rect()
    text1.center = (750, 50)
    WINDOW.blit(Rscore, text1)

    pygame.display.update()

def bounce(ball, leftPaddle, rightPaddle):
    if (ball.x > 50 and ball.x < 60 and ball.y > leftPaddle.y and ball.y - leftPaddle.y < 60):
        ball.bounce()
    if (ball.x < 760 and ball.x > 750 and ball.y > rightPaddle.y and ball.y - rightPaddle.y < 60):
        ball.bounce()

def goal_check(ball, leftPaddle, rightPaddle, leftScore, rightScore):
    if ball.x < 0:
        rightScore += 1
        ball.reset()
        leftPaddle.reset(True)
        rightPaddle.reset(False)
    elif ball.x > 800:
        leftScore += 1
        ball.reset()
        leftPaddle.reset(True)
        rightPaddle.reset(False)
    return leftScore, rightScore

def main(window):
    clock = pygame.time.Clock()
    run = True

    paddles = [Paddle(50,400), Paddle(750,400)]
    ball = Ball(400,400, random.choice([-3, -2, 2, 3]), random.choice([-3,-2, 2, 3]))
    leftScore = 0
    rightScore = 0
    font = pygame.font.Font('freesansbold.ttf', 50)
    
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
        bounce(ball, paddles[0], paddles[1])
        leftScore, rightScore = goal_check(ball, paddles[0], paddles[1], leftScore, rightScore)
        draw(window, paddles, ball, leftScore, rightScore)
        

if __name__ == "__main__":
    main(WINDOW)
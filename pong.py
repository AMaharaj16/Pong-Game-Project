import pygame

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


def draw(window, paddle):
    window.fill(BLACK)
    paddle.draw(window)
    pygame.display.update()

    

def main(window):
    clock = pygame.time.Clock()
    run = True

    paddle = Paddle(50,400)
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        keys = pygame.key.get_pressed()
        paddle.move(up=keys[pygame.K_UP], down=keys[pygame.K_DOWN])
        draw(window, paddle)


if __name__ == "__main__":
    main(WINDOW)
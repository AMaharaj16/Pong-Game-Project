import pygame

pygame.init()
pygame.display.set_caption("Pong Game in Python")
HEIGHT = 800
WIDTH = 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
HEIGHT_PADDLE = 60
WIDTH_PADDLE = 10
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = HEIGHT_PADDLE
        self.width = WIDTH_PADDLE

    def draw(self,window):
        pygame.draw.rect(window, WHITE, (self.x, self.y, WIDTH_PADDLE, HEIGHT_PADDLE))


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
        draw(window, paddle)


if __name__ == "__main__":
    main(WINDOW)
import pygame
import time

pygame.init()

WIN_WIDTH = 280
WIN_HEIGHT = 500

GROUND_HEIGHT = 400

SWING = 0.3

background_image = pygame.image.load("background.png")
ground_image = pygame.image.load("ground.png")
pipe_image = pygame.image.load("pipe.png")
bird1_image = pygame.image.load("bird1.png")
bird2_image = pygame.image.load("bird2.png")
bird3_image = pygame.image.load("bird3.png")

window_size = (WIN_WIDTH, WIN_HEIGHT)

screen = pygame.display.set_mode(window_size)

class FlappyBird:
    def __init__(self):
        self.x = WIN_WIDTH / 3
        self.y = WIN_HEIGHT / 2
        self.score = 0
        self.drawBackground()
        self.choose_bird = 0
        self.move_ground = 0


    def reset(self):
        self.y = WIN_HEIGHT / 2
        self.score = 0

    def drawBird(self):
        if pygame.display.get_surface() is None:
            return

        if self.choose_bird == 0:
            screen.blit(bird1_image, (self.x, self.y))
            self.choose_bird = 1
            time.sleep(SWING)
        elif self.choose_bird == 1:
            screen.blit(bird2_image, (self.x,self.y))
            self.choose_bird = 2
            time.sleep(SWING)
        elif self.choose_bird == 2:
            screen.blit(bird3_image, (self.x,self.y))
            self.choose_bird = 3
            time.sleep(SWING)
        elif self.choose_bird == 3:
            screen.blit(bird2_image,(self.x,self.y))
            self.choose_bird = 0
            time.sleep(SWING)
        else:
            screen.blit(bird1_image, (self.x, self.y))

    def drawPipe(self):
        pass

    def drawBackground(self):
        screen.blit(background_image, (0, 0))

    def drawGround(self):
        screen.blit(ground_image, (0 - self.move_ground,GROUND_HEIGHT))
        screen.blit(ground_image, (WIN_WIDTH - 15 - self.move_ground,GROUND_HEIGHT))
        self.move_ground += 5
        if (self.move_ground > WIN_WIDTH):
            self.move_ground = 0

    def drawScore(self):
        pass

    def game_loop(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
            self.drawBird()
            self.drawGround()
            pygame.display.update()

def main():
    game = FlappyBird()
    game.game_loop()

main()



import pygame
import random

pygame.init()
clock = pygame.time.Clock()

WIN_WIDTH = 280
WIN_HEIGHT = 500

FPS = 1

BLACK = (0,0,0)

GROUND_HEIGHT = 400
GROUND_SPEED = 2

SWING = 20


background_image = pygame.image.load("background.png")
ground_image = pygame.image.load("ground.png")
pipe_image = pygame.image.load("pipe.png")
bird1_image = pygame.image.load("bird1.png")
bird2_image = pygame.image.load("bird2.png")
bird3_image = pygame.image.load("bird3.png")

rotaded_pipe = pygame.transform.rotate(pipe_image, 180)

window_size = (WIN_WIDTH, WIN_HEIGHT)

screen = pygame.display.set_mode(window_size)

class FlappyBird:
    def __init__(self):
        self.x = WIN_WIDTH / 3
        self.drawBackground()
        self.choose_bird = 0
        self.move_ground = 0
        self.swing = 0
        self.pipe_x = 400
        self.pipe = []
        self.pipe_up = []
        self.next_pipe = 100

    def reset(self):
        self.y = WIN_HEIGHT / 2
        self.score = 0
        self.new_pipe = 0

    def drawBird(self):
        if pygame.display.get_surface() is None:
            return

        if self.choose_bird == 0:
            screen.blit(bird1_image, (self.x, self.y))
            self.swing += 1
            if self.swing == SWING:
                self.choose_bird = 1
                self.swing = 0
        elif self.choose_bird == 1:
            screen.blit(bird2_image, (self.x,self.y))
            self.swing += 1
            if self.swing == SWING:
                self.choose_bird = 2
                self.swing = 0
        elif self.choose_bird == 2:
            screen.blit(bird3_image, (self.x,self.y))
            self.swing += 1
            if self.swing == SWING:
                self.choose_bird = 3
                self.swing = 0
        elif self.choose_bird == 3:
            screen.blit(bird2_image,(self.x,self.y))
            self.swing += 1
            if self.swing == SWING:
                self.choose_bird = 0
                self.swing = 0
        else:
            screen.blit(bird1_image, (self.x, self.y))

    def drawPipe(self):
        self.pipe_y = random.randint(100, 380)
        self.pipe.append((self.pipe_x, self.pipe_y))
        self.pipe_up.append((self.pipe_x, self.pipe_y - 430))
        for pipes_list in self.pipe:
            screen.blit(pipe_image, (pipes_list[0], pipes_list[1]))
        for pipesup_list in self.pipe_up:
            screen.blit(rotaded_pipe, (pipesup_list[0], pipesup_list[1]))

    def movePipe(self):
        for pipes_list in self.pipe:
            index = self.pipe.index(pipes_list)
            self.pipe[index] = (pipes_list[0] - int(GROUND_SPEED), pipes_list[1])
            screen.blit(pipe_image, (pipes_list[0], pipes_list[1]))
            if pipes_list[0] < -50:
                del self.pipe[index]

    def movePipeUp(self):
        for pipes_up in self.pipe_up:
            index_up = self.pipe_up.index(pipes_up)
            self.pipe_up[index_up] = (pipes_up[0] - int(GROUND_SPEED), pipes_up[1])
            screen.blit(rotaded_pipe, (pipes_up[0], pipes_up[1]))
            if pipes_up[0] < -50:
                del self.pipe_up[index_up]

    def drawBackground(self):
        screen.blit(background_image, (0, 0))

    def drawGround(self):
        screen.blit(ground_image, (0 - self.move_ground,GROUND_HEIGHT))
        screen.blit(ground_image, (WIN_WIDTH - 15 - self.move_ground,GROUND_HEIGHT))
        self.move_ground += GROUND_SPEED
        if (self.move_ground > WIN_WIDTH):
            self.move_ground = 0

    def drawScore(self):
        self.font = pygame.font.Font(None, 25)
        self.score_text = self.font.render(f"Score: {self.score}", True, BLACK)
        screen.blit(self.score_text, (10,10))

    def game_loop(self):
        clock.tick(FPS)
        self.reset()
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()   
            self.drawBackground() 
            self.drawBird()
            self.movePipe()
            self.movePipeUp()
            if self.new_pipe == self.next_pipe:
                self.drawPipe()
                self.new_pipe = 0
            self.new_pipe += 1
            self.drawGround()
            self.drawScore() 
            pygame.display.update()

def main():
    game = FlappyBird()
    game.game_loop()

main()



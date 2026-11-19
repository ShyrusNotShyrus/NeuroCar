from settings import TITLE, FPS, TRACK
from car import Car
import pygame

class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.running = True
        self.clock = pygame.time.Clock()

        track_image = pygame.image.load(TRACK)
        self.width, self.height = track_image.get_size()
        self.screen = pygame.display.set_mode((self.width,self.height))

        self.car = Car(0,0)


    def run(self):
        while self.running:
            self.update()
            self.clock.tick(FPS)
            self.draw_track("assets/track1.PNG")
            self.handle_events()

        pygame.quit()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.car.throttle()
        else:
            self.car.apply_friction()

        if keys[pygame.K_a]:
            self.car.turn(1)
        if keys[pygame.K_d]:
            self.car.turn(-1)
            
        self.car.move()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def draw_track(self, track):
        self.background = pygame.image.load(track).convert()
        self.screen.blit(self.background, (0, 0))
        self.car.draw(self.screen)                
        pygame.display.flip() 
from settings import TITLE, FPS, TRACK
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


    def run(self):
        while self.running:
            self.update()
            self.clock.tick(FPS)
            self.draw_track("assets/track1.PNG")
            self.handle_events()

        pygame.quit()

    def update(self):
        pass

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def draw_track(self, track):
        self.background = pygame.image.load(track).convert()
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip() 
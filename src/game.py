from settings import TITLE, FPS, TRACK, START_END_COLOR
from car import Car
import pygame

class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.running = True
        self.clock = pygame.time.Clock()
        self.background = None

        self.track_image = pygame.image.load(TRACK)
        self.width, self.height = self.track_image.get_size()
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.start_end_pixels = []

        self.car = Car(self.determine_car_spawn_position(), self.determine_car_spawn_rotation())


    def run(self):
        while self.running:
            self.update()
            self.clock.tick(FPS)
            self.draw_track(TRACK)
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


    def determine_car_spawn_position(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.track_image.get_at((i,j))[:3] == START_END_COLOR:
                    self.start_end_pixels.append((i,j))

        # Get middle point
        mid_x = sum(x for x, y in self.start_end_pixels) / len(self.start_end_pixels)
        mid_y = sum(y for x, y in self.start_end_pixels) / len(self.start_end_pixels)

        return (mid_x, mid_y)

    def determine_car_spawn_rotation(self):
        xs = [x for x, y in self.start_end_pixels]
        ys = [y for x, y in self.start_end_pixels]

        width = max(xs) - min(xs)
        height = max(ys) - min(ys)

        start_angle = 0
        if width > height:
            start_angle = 90

        return start_angle



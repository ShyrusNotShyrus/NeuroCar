from settings import PLAYER1_CAR_IMAGE, CAR_MAX_SPEED, CAR_ACCELERATION, CAR_FRICTION, CAR_TURN_SPEED
import pygame
import math
from PIL import Image

class Car:

    def __init__(self, pos, angle):
        
        self.image = self.initialize_car_iamge(PLAYER1_CAR_IMAGE)

        x_offset = 0
        y_offset = 0

        if angle == 0:
            x_offset = -30
            y_offset = 0
        else:
            x_offset = 0
            y_offset = 25

        self.x = pos[0] + x_offset
        self.y = pos[1] + y_offset
        self.speed = 0
        self.speed = 0
        self.angle = angle
        
        return

    def initialize_car_iamge(self, image):
        image = pygame.image.load(PLAYER1_CAR_IMAGE).convert_alpha()
        return pygame.transform.scale(image, (55, 25))  


    def draw(self, screen):
        rotated = pygame.transform.rotate(self.image, self.angle)
        rect = rotated.get_rect(center=(self.x, self.y))
        screen.blit(rotated, rect)

    def throttle(self):
        self.speed = min(self.speed + CAR_ACCELERATION, CAR_MAX_SPEED)

    def apply_friction(self):
        self.speed = max(self.speed - CAR_FRICTION, 0)        

    def turn(self, direction):
        if self.speed > 0:
            self.angle += CAR_TURN_SPEED * direction

    def move(self):
        rad = math.radians(self.angle)
        self.x += math.cos(rad) * self.speed
        self.y -= math.sin(rad) * self.speed 



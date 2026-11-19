from settings import PLAYER1_CAR_IMAGE, CAR_MAX_SPEED, CAR_ACCELERATION, CAR_FRICTION, CAR_TURN_SPEED
import pygame
import math
from PIL import Image

class Car:

    def __init__(self, x, y):
        
        self.image = self.initialize_car_iamge(PLAYER1_CAR_IMAGE)
        self.x = x
        self.y = y
        self.speed = 0
        self.speed = 0
        self.angle = 0
        
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



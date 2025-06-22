import pygame
from circleshape import CircleShape
from constants import SHOOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, SHOOT_RADIUS, 2)

    def update (self, dt):
        self.position += self.velocity * dt
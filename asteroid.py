import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius, asteriod_group):
        super().__init__(x, y, radius)
        self.asteriod_group = asteriod_group

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update (self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            vector_one = self.velocity.rotate(random_angle)
            vector_two = self.velocity.rotate(-random_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteriod_one = Asteroid(self.position.x, self.position.y, new_radius, self.asteriod_group)
            new_asteriod_two = Asteroid(self.position.x, self.position.y, new_radius, self.asteriod_group)

            new_asteriod_one.velocity = vector_one * 1.2
            new_asteriod_two.velocity = vector_two * 1.2
            self.asteriod_group.add(new_asteriod_one)
            self.asteriod_group.add(new_asteriod_two)
             
            

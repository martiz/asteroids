import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (LINE), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_velocity = self.velocity * 1.2

        Asteroid(self.position.x, self.position.y, new_radius).velocity = new_velocity.rotate(random_angle)
        Asteroid(self.position.x, self.position.y, new_radius).velocity = new_velocity.rotate(-random_angle)

        # Boots' solution ---
        # a = self.velocity.rotate(random_angle)
        # b = self.velocity.rotate(-random_angle)
        # asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        # asteroid.velocity = a * 1.2
        # asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        # asteroid.velocity = b * 1.2

import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    # Check for collision with another CircleShape object
    def collide(self, other):
        # Calculate the distance between the two CircleShape objects
        distance = self.position.distance_to(other.position)
        # Collision occurs if the distance is less than or equal to the sum of their radii
        return distance <= (self.radius + other.radius)

    # Boots' solution ---
    # def collides_with(self, other):
    #     return self.position.distance_to(other.position) <= self.radius + other.radius

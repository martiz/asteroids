import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    fps_clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # player.update(dt)
        for obj in updatable:
            obj.update(dt)

        # asteroids / collision check
        for asteroid in asteroids:
            if player.collide(asteroid):
                sys.exit("Game over!")
            for shot in shots:
                if shot.collide(asteroid):
                    # pygame.sprite.Sprite.kill(self.shot, self.asteroid)
                    shot.kill()
                    asteroid.split()
        
        # Boots' solution ---
            # if asteroid.collides_with(player):
                # print("Game over!")
                # sys.exit()

        screen.fill((BACKGROUND))
        
        # player.draw(screen)
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        
        dt = fps_clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()

import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable,)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    AsteroidField()
    dt = 0
    while True:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            return
        screen.fill((0, 0, 0))
        for updatable_sprite in updatable:
           updatable_sprite.update(dt)
        for drawable_sprite in drawable:
           drawable_sprite.draw(screen)
        for asteroid in asteroids:
          if asteroid.check_for_collisions(player):
            print("Game Over!")
            sys.exit()
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots)
    asteroidfield = AsteroidField(asteroids)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0,0,0))

        for element in updateable:
            element.update(dt)

        for asteriod in asteroids:
            if asteriod.collision(player):
                print("Game over!")
                return
            else:
                for shot in shots:
                    if asteriod.collision(shot):
                        asteriod.split()
                        shot.kill()

        for element in drawable:
            element.draw(screen)
        
        for shot in shots:
            shot.update(dt)
            shot.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
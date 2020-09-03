import pygame

pygame.init()

# Variables
FPS = 30
game_clock = pygame.time.Clock()

# Animation loop
while True:
    #iterate through list of frames, printing new one each time

    pygame.display.update()
    game_clock.tick(FPS)

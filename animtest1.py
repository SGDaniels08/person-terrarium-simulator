import pygame, sys
from pygame.locals import *

pygame.init()

# Variables
FPS = 30
game_clock = pygame.time.Clock()
frames_list = []

# Add each frame to frames_list
for i in range(24):
    individual_frame = pygame.image.load("frame" + str(i) +".png")
    frames_list.append(individual_frame)

# Create main surface
DISPLAYSURF = pygame.display.set_mode((1000, 1000))

# Animation loop
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #iterate through list of frames, printing new one each time
    DISPLAYSURF.blit(frames_list[0], (50, 50))

    pygame.display.update()
    game_clock.tick(FPS)

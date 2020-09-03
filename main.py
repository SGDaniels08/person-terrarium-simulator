# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pygame,sys
from pygame.locals import *


def print_terrarium():
    pygame.init()

    # simple colors
    black = (0, 0, 0)
    white = (255, 255, 255)

    # World screen
    world_size = (1200, 750)
    world = pygame.display.set_mode(world_size)
    world_background_color = (172, 221, 231)
    world.fill(world_background_color)

    # Terrarium elements
    terrarium_origin_x = 100
    terrarium_origin_y = 150
    terrarium_width = 900
    terrarium_height = 500
    sand_color = (210, 180, 140)
    sand = pygame.Surface((terrarium_width, 300))
    sand.fill(sand_color)

    glass_color = (255, 255, 255)
    glass = pygame.Surface((terrarium_width, 200))
    glass.fill(glass_color)

    # Blit them together
    sand_origin_x = terrarium_origin_x
    sand_origin_y = terrarium_origin_y + 200
    world.blit(glass, (terrarium_origin_x, terrarium_origin_y))
    world.blit(sand, (sand_origin_x, sand_origin_y))
    pygame.draw.line(world, black, (sand_origin_x, sand_origin_y),
                     (sand_origin_x + terrarium_width, sand_origin_y), 2)

    # Oval for sizing
    person_height = 75
    person_width = 20
    person_box = pygame.Surface((person_width, person_height), pygame.SRCALPHA, 32)
    person_origin_x = 300
    person_origin_y = sand_origin_y - person_height
    pygame.draw.ellipse(person_box, black, (0, 0, person_width, person_height))
    world.blit(person_box, (person_origin_x, person_origin_y))

    # Text
    game_font = pygame.font.SysFont("Lucida Console", 36)
    game_text = game_font.render("Graaaaaassssss... tastes bad!", 1, black)
    world.blit(game_text, (25, 25))

    # Put frames in list
    walking_frames = []
    for i in range(12):
        image_path = "frame" + str(i) + ".png"
        im = pygame.image.load(image_path)
        walking_frames.append(im)
        
    # Close program box

    # Game loop
    clock = pygame.time.Clock()
    frame_count = 0
    while True:
        clock.tick(24)

        # Test events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Animation
        world.blit(walking_frames[frame_count], (10, 10))

        frame_count += 1
        if frame_count == 12:
            frame_count = 0

        pygame.display.update()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_terrarium()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

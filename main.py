# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pygame


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
    person_origin_x = 300
    person_origin_y = sand_origin_y - person_height
    pygame.draw.ellipse(world, black, (person_origin_x, person_origin_y, person_width, person_height))

    pygame.display.update()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_terrarium()
    input()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
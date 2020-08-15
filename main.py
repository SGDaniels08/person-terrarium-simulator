# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pygame


def print_terrarium():
    pygame.init()

    #World screen
    world = pygame.display.set_mode((1000, 700))
    world.fill((172, 221, 231))

    #Terrarium elements
    sand = pygame.Surface((700, 400))
    sand.fill((210, 180, 140))
    glass = pygame.Surface((700, 200))
    glass.fill((255, 255, 255))

    #Blit them together
    world.blit(glass, (100, 50))
    world.blit(sand, (100, 250))
    pygame.draw.line(world, (0, 0, 0), (100, 250), (800, 250), 2)

    #Oval for sizing
    pygame.draw.ellipse(world, (0, 0, 0), (300, 170, 30, 80))

    pygame.display.update()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_terrarium()
    input()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import pygame

pygame.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode((800, 512), pygame.SRCALPHA, 32)

class Animate:
    def __init__ (self, xx, yy):
        self.xpos = xx       # Position to place the animation
        self.ypos = yy
        self.frames = ()     # Images for this animation
        self.nextFrames = 0  # Next frame to be played
        self.Nframes = 0     # Total number of frames
        self.soundName = ""  # Name of the sound file for this animation
        self.playing = False
    """
    def play (self):
    def stop (self):
    def pause (self):
    def setPosition (self, x, y):
    def getPosition (self, x, y):
    def setSoundName (self, s):
    def addFrame (self, p):
    def draw (self):
    """

ac = Animate(100, 100)

for i in range(24):
    im = pygame.image.load("frame" + str(i) + ".png")
    ac.addFrame(im)

ac.play()

while True:
    clock.tick(24)
    ac.draw()
    pygame.display.update()

""" Main module """
import pygame
from .classes import classes

background = pygame.image.load("background.png")

white = (255, 255, 255)
W = 640
H = 480
screen = pygame.display.set_mode((W, H))
pygame.mixer.init()

background = pygame.transform.scale(background, (W, H))

RUN = True

tree = classes.Tree()
bird = classes.Bird()
rat = classes.Rat()

listObjects = [tree, bird, rat]

while RUN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
    screen.fill((white))
    screen.blit(background,(0,0))
    pygame.display.update()
    for obj in listObjects:
        obj.draw(screen)
        obj.do_action()

pygame.quit()

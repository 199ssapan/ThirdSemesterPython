""" This module contains classes to call class methods """
import pygame

class Object:
    """ Object abstract class """
class Tree(Object):
    """ Tree class """
    def draw(self, screen):
        """ Draws tree """
        tree = pygame.image.load("tree.png")
        tree = pygame.transform.scale(tree, (150, 150))
        screen.blit(tree,(100, 100))
        pygame.display.update()
        pygame.time.delay(1000)
    def do_action(self):
        """ Plays tree's sound """
        pygame.mixer.music.load("treesound.mp3")
        pygame.mixer.music.play()
        pygame.time.delay(1000)
class Creature(Object):
    """ Creature abstract class """
class Rat(Creature):
    """ Rat class"""
    def draw(self, screen):
        """ Draws rat """
        rat = pygame.image.load("rat.png")
        rat = pygame.transform.scale(rat, (110, 110))
        screen.blit(rat,(270, 350))
        pygame.display.update()
    def do_action(self):
        """ Plays rat's sound """
        pygame.mixer.music.load("ratsound.mp3")
        pygame.mixer.music.play()
        pygame.time.delay(1000)
class Bird(Creature):
    """ Bird class """
    def draw(self, screen):
        """ Draws bird """
        bird = pygame.image.load("bird.png")
        bird = pygame.transform.scale(bird, (100, 100))
        screen.blit(bird,(250,250))
        pygame.display.update()
        pygame.time.delay(1000)
    def do_action(self):
        """ Plays bird's sound """
        pygame.mixer.music.load("birdsound.mp3")
        pygame.mixer.music.play()
        pygame.time.delay(1000)

import pygame
from pygame.locals import *
import sys
import random
from tkinter import filedialog
from tkinter import *

pygame.init()

vec = pygame.math.Vector2
HEIGHT = 350
WIDTH = 700
ACC = 0.3
FRIC = -0.10
FPS = 60
FPS_CLOCK = pygame.time.Clock()
COUNT = 0

displaysurface = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Game")

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
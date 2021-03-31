# The class for food object
from random import random
from core import screen_height, screen_width, red
import pygame as pg


class Food():
    # Initialization
    def __init__(self):

        self.x = screen_width/2
        self.y = screen_height/4
        self.color = red
        self.width = 10
        self.height = 10
        self.food = pg.Rect(self.x, self.y, self.width, self.height)


    # Makes the food visible
    def draw_food(self, surface):
        pg.draw.rect(surface, self.color, self.food)


    # Is the food eaten?
    def is_eaten(self, head):
        return self.food.colliderect(head)
    # Returns a new position for the food after it is eaten
    def new_pos(self):
        self.x = random.randint(0,screen_width-self.width)
        self.y = random.randint(0,screen_height-self.height)
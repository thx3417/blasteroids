import pygame
from asteroid import *

class Shot(Asteroid):

	containers = None

	def __init(self, x, y, radius):
		super().__init__(x, y, radius)


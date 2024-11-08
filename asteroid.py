import pygame
from circleshape import *
from constants import *

class Asteroid(CircleShape):

	containers = None

	def __init(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen, color = "white", line_width = 2):
		pygame.draw.circle(screen, color, self.position, self.radius, line_width)

	def update(self, dt):
		self.position += self.velocity * dt

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		

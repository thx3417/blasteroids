import pygame
import random
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
		random_angle = random.uniform(20, 50)
		minus = self.velocity.rotate(-random_angle)
		plus = self.velocity.rotate(random_angle)
		new_radius = self.radius - ASTEROID_MIN_RADIUS
		child_plus = Asteroid(self.position.x, self.position.y, new_radius)
		child_plus.velocity = plus * 1.2
		child_minus = Asteroid(self.position.x, self.position.y, new_radius)
		child_minus.velocity = minus * 1.2


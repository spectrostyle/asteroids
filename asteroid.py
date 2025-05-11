import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

	def update(self, dt):
		self.position += (self.velocity * dt)

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return

		random_angle = random.uniform(20, 50)
		positive_vector = self.velocity.rotate(random_angle)
		negative_vector = self.velocity.rotate(-random_angle)
		new_radius = self.radius - ASTEROID_MIN_RADIUS

		asteroid_1 = Asteroid(x=self.position.x, y=self.position.y, radius=new_radius)
		asteroid_2 = Asteroid(x=self.position.x, y=self.position.y, radius=new_radius)

		asteroid_1.velocity = positive_vector * 1.2
		asteroid_2.velocity = negative_vector * 1.2

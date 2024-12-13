import pygame
from constants import SHOT_RADIUS
from circleshape import CircleShape

class Shot(CircleShape):
  def __init__(self, x, y, radius):
    super().__intit__(self, x, y, radius)
    self.x = x
    self.y = y
    self.radius = radius

  def draw(self, screen):
    pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)

  def update(self, dt):
    self.position += self.velocity * dt


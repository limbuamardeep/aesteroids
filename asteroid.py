import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH,ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white",self.position ,self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position+=self.velocity*dt

    def split(self):
        self.kill()
        if self.radius<=ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_value=random.uniform(20,50)
        vector1=self.velocity.rotate(random_value)
        vector2=self.velocity.rotate(-random_value)
        new_radius=self.radius-ASTEROID_MIN_RADIUS
        asteroid1=Asteroid(self.position.x,self.position.y,new_radius)
        asteroid1.velocity=vector1*1.2
        asteroid2=Asteroid(self.position.x,self.position.y,new_radius)
        asteroid2.velocity=vector2*1.2
        


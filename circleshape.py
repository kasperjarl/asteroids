import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collisions(self, other_circle_obj):
        dist = pygame.math.Vector2.distance_to(self.position, other_circle_obj.position)
        return dist <= self.radius + other_circle_obj.radius
    
    def bullet_collision(self, bullet):
        dist = pygame.math.Vector2.distance_to(self.position, bullet.position)
        return dist <= self.radius + bullet.radius

    
    
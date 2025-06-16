import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, speed=10, piercing=False):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center=position)
        self.speed = speed
        self.piercing = piercing

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()

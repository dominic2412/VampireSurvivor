import pygame

from .constants import BULLET_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT


class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, velocity):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect(center=position)
        self.velocity = velocity

    def update(self):
        self.rect.x += self.velocity[0] * BULLET_SPEED
        self.rect.y += self.velocity[1] * BULLET_SPEED
        if (
            self.rect.right < 0
            or self.rect.left > SCREEN_WIDTH
            or self.rect.bottom < 0
            or self.rect.top > SCREEN_HEIGHT
        ):
            self.kill()

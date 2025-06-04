import pygame

from .bullet import Bullet
from .constants import PLAYER_SPEED


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(400, 300))
        self.health = 100
        self.bullets = pygame.sprite.Group()
        self._last_shot = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
        if keys[pygame.K_UP]:
            self.rect.y -= PLAYER_SPEED
        if keys[pygame.K_DOWN]:
            self.rect.y += PLAYER_SPEED

        now = pygame.time.get_ticks()
        if now - self._last_shot > 500:
            self.shoot()
            self._last_shot = now
        self.bullets.update()

    def shoot(self):
        bullet = Bullet(self.rect.center, (1, 0))
        self.bullets.add(bullet)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        self.bullets.draw(surface)

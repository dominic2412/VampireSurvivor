import pygame

from .constants import ENEMY_SPEED


class Enemy(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(center=position)

    def update(self, player_pos):
        dx = player_pos[0] - self.rect.centerx
        dy = player_pos[1] - self.rect.centery
        distance = (dx ** 2 + dy ** 2) ** 0.5 or 1
        self.rect.x += int(ENEMY_SPEED * dx / distance)
        self.rect.y += int(ENEMY_SPEED * dy / distance)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

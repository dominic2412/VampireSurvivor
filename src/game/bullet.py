import pygame

class Bullet(pygame.sprite.Sprite):
    """Projectile fired by the player."""

    def __init__(self, position, direction=(0, -1), speed=10, piercing=False):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center=position)
        self.speed = speed
        # Normalise direction to ensure consistent speed
        self.direction = pygame.math.Vector2(direction)
        if self.direction.length() == 0:
            self.direction = pygame.math.Vector2(0, -1)
        else:
            self.direction = self.direction.normalize()
        self.piercing = piercing

    def update(self):
        move = self.direction * self.speed
        self.rect.x += int(move.x)
        self.rect.y += int(move.y)
        # Remove bullet when it goes off screen
        if (
            self.rect.right < 0
            or self.rect.left > 800
            or self.rect.bottom < 0
            or self.rect.top > 600
        ):
            self.kill()

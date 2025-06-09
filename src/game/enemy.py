import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, position, speed=2):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(center=position)
        self.speed = speed

    def update(self, target_pos):
        """Move toward the given target position."""
        direction = pygame.math.Vector2(target_pos) - self.rect.center
        if direction.length() != 0:
            direction = direction.normalize() * self.speed
            self.rect.centerx += int(direction.x)
            self.rect.centery += int(direction.y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class FastEnemy(Enemy):
    """A quicker enemy that is smaller and moves faster."""

    def __init__(self, position, speed=4):
        super().__init__(position, speed)
        self.image = pygame.Surface((30, 30))
        self.image.fill((0, 128, 255))
        self.rect = self.image.get_rect(center=position)


class StrongEnemy(Enemy):
    """An enemy that requires several hits to defeat."""

    def __init__(self, position, speed=1, health=3):
        super().__init__(position, speed)
        self.image = pygame.Surface((50, 50))
        self.image.fill((128, 0, 0))
        self.rect = self.image.get_rect(center=position)
        self.health = health
        

class BossEnemy(Enemy):
    """A tough enemy that takes many hits to defeat."""

    def __init__(self, position, speed=1, health=5):
        super().__init__(position, speed)
        self.image = pygame.Surface((60, 60))
        self.image.fill((128, 0, 128))
        self.rect = self.image.get_rect(center=position)
        self.health = health


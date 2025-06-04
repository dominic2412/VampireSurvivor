import pygame


class Enemy(pygame.sprite.Sprite):
    """Simple enemy that slowly moves toward the player."""

    def __init__(self, position: tuple[int, int]):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(center=position)

    def update(self, target: tuple[int, int]) -> None:
        """Move slightly toward the target position."""
        if self.rect.centerx < target[0]:
            self.rect.x += 1
        elif self.rect.centerx > target[0]:
            self.rect.x -= 1

        if self.rect.centery < target[1]:
            self.rect.y += 1
        elif self.rect.centery > target[1]:
            self.rect.y -= 1

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, self.rect)

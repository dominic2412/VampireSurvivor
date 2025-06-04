import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(center=position)

    def update(self):
        pass

    def draw(self, surface):
        surface.blit(self.image, self.rect)

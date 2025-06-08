import pygame

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, position, heal_amount=1):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect(center=position)
        self.heal_amount = heal_amount

    def update(self):
        pass

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


class ShieldPowerUp(PowerUp):
    """Power-up granting temporary invincibility."""

    def __init__(self, position, duration=180):
        super().__init__(position, heal_amount=0)
        self.image.fill((0, 255, 255))
        self.shield_duration = duration


class SpeedPowerUp(PowerUp):
    """Power-up giving the player a short speed boost."""

    def __init__(self, position, duration=180):
        super().__init__(position, heal_amount=0)
        self.image.fill((255, 165, 0))
        self.speed_duration = duration


import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, health=3):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(400, 300))
        self.health = health

    def take_damage(self, amount=1):
        self.health -= amount

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

        # Keep player on screen
        self.rect.clamp_ip(pygame.Rect(0, 0, 800, 600))

    def draw(self, surface):
        surface.blit(self.image, self.rect)

import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, health=3, max_health=5, base_speed=5):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(400, 300))
        self.health = health
        self.max_health = max_health
        self.shield_timer = 0
        self.speed_timer = 0
        self.triple_shot_timer = 0
        self.freeze_timer = 0
        self.pierce_timer = 0
        self.homing_timer = 0
        self.bullet_speed_timer = 0
        self.base_speed = base_speed

    def take_damage(self, amount=1):
        if self.shield_timer <= 0:
            self.health -= amount

    def heal(self, amount=1):
        self.health = min(self.health + amount, self.max_health)

    def increase_max_health(self, amount=1):
        """Increase maximum health and heal the player."""
        self.max_health += amount
        self.health = self.max_health

    def add_shield(self, duration=180):
        self.shield_timer = duration

    def add_speed(self, duration=180):
        self.speed_timer = duration

    def add_triple_shot(self, duration=180):
        self.triple_shot_timer = duration

    def add_freeze(self, duration=180):
        self.freeze_timer = duration

    def add_pierce(self, duration=180):
        self.pierce_timer = duration

    def add_homing(self, duration=180):
        self.homing_timer = duration

    def add_bullet_speed(self, duration=180):
        """Increase bullet speed for a short time."""
        self.bullet_speed_timer = duration



    def update(self):
        keys = pygame.key.get_pressed()
        move_speed = self.base_speed + 3 if self.speed_timer > 0 else self.base_speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= move_speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += move_speed
        if keys[pygame.K_UP]:
            self.rect.y -= move_speed
        if keys[pygame.K_DOWN]:
            self.rect.y += move_speed

        # Keep player on screen
        self.rect.clamp_ip(pygame.Rect(0, 0, 800, 600))

        if self.shield_timer > 0:
            self.shield_timer -= 1
        if self.speed_timer > 0:
            self.speed_timer -= 1
        if self.triple_shot_timer > 0:
            self.triple_shot_timer -= 1
        if self.freeze_timer > 0:
            self.freeze_timer -= 1
        if self.pierce_timer > 0:
            self.pierce_timer -= 1
        if self.homing_timer > 0:
            self.homing_timer -= 1
        if self.bullet_speed_timer > 0:
            self.bullet_speed_timer -= 1


    def draw(self, surface):
        surface.blit(self.image, self.rect)

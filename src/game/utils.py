import pygame


def handle_bullet_enemy_collisions(bullets, enemies):
    """Handle bullet/enemy collisions and return number of enemies removed."""
    collisions = pygame.sprite.groupcollide(bullets, enemies, True, True)
    return sum(len(v) for v in collisions.values())

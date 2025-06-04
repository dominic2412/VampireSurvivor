import pygame


def handle_bullet_enemy_collisions(bullets, enemies):
    """Handle bullet/enemy collisions and return number of enemies removed."""
    collisions = pygame.sprite.groupcollide(bullets, enemies, True, True)
    return sum(len(v) for v in collisions.values())


def handle_player_enemy_collisions(player, enemies):
    """Damage the player if any enemies collide with them."""
    collided = pygame.sprite.spritecollide(player, enemies, True)
    if collided:
        player.take_damage()
        return True
    return False

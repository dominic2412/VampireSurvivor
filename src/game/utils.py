import pygame


def handle_bullet_enemy_collisions(bullets, enemies):
    """Handle bullet/enemy collisions and return number of enemies removed."""
    collisions = pygame.sprite.groupcollide(bullets, enemies, True, False)
    killed = 0
    for enemy_list in collisions.values():
        for enemy in enemy_list:
            if hasattr(enemy, "health"):
                enemy.health -= 1
                if enemy.health <= 0:
                    enemy.kill()
                    killed += 1
            else:
                enemy.kill()
                killed += 1
    return killed


def handle_player_enemy_collisions(player, enemies):
    """Damage the player if any enemies collide with them."""
    collided = pygame.sprite.spritecollide(player, enemies, True)
    if collided:
        player.take_damage()
        return True
    return False


def handle_player_powerup_collisions(player, powerups):
    """Heal the player if they collect a power-up."""
    collided = pygame.sprite.spritecollide(player, powerups, True)
    if collided:
        player.heal()
        return True
    return False

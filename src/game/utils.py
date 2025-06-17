import pygame


def handle_bullet_enemy_collisions(bullets, enemies):
    """Handle bullet/enemy collisions and return number of enemies removed."""
    collisions = pygame.sprite.groupcollide(bullets, enemies, False, False)
    killed = 0
    for bullet, enemy_list in collisions.items():
        for enemy in enemy_list:
            if hasattr(enemy, "health"):
                enemy.health -= 1
                if enemy.health <= 0:
                    enemy.kill()
                    killed += 1
            else:
                enemy.kill()
                killed += 1
        if not getattr(bullet, "piercing", False):
            bullet.kill()
    return killed


def handle_player_enemy_collisions(player, enemies):
    """Damage the player if any enemies collide with them."""
    collided = pygame.sprite.spritecollide(player, enemies, True)
    if collided:
        player.take_damage()
        return True
    return False


def handle_player_powerup_collisions(player, powerups):
    """Apply effects from collected power-ups."""
    collided = pygame.sprite.spritecollide(player, powerups, True)
    collected = False
    for powerup in collided:
        if hasattr(powerup, "heal_amount") and powerup.heal_amount:
            player.heal(powerup.heal_amount)
            collected = True
        if hasattr(powerup, "shield_duration"):
            player.add_shield(powerup.shield_duration)
            collected = True
        if hasattr(powerup, "speed_duration"):
            player.add_speed(powerup.speed_duration)
            collected = True
        if hasattr(powerup, "triple_duration"):
            player.add_triple_shot(powerup.triple_duration)
            collected = True
        if hasattr(powerup, "freeze_duration"):
            player.add_freeze(powerup.freeze_duration)
            collected = True
        if hasattr(powerup, "pierce_duration"):
            player.add_pierce(powerup.pierce_duration)
            collected = True
        if hasattr(powerup, "homing_duration"):
            player.add_homing(powerup.homing_duration)
            collected = True


    return collected


import random
import pygame
from game.player import Player
from game.enemy import Enemy, FastEnemy, StrongEnemy, BossEnemy
from game.bullet import Bullet
from game.powerup import (
    PowerUp,
    ShieldPowerUp,
    SpeedPowerUp,
    TripleShotPowerUp,
    FreezePowerUp,

    PiercePowerUp,
    MaxHealthPowerUp,
    HomingPowerUp,
    RapidFirePowerUp,
)

from game.utils import (
    handle_bullet_enemy_collisions,
    handle_player_enemy_collisions,
    handle_player_powerup_collisions,
)


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Vampire Survivor")
    clock = pygame.time.Clock()

    player = Player()
    player_group = pygame.sprite.GroupSingle(player)
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    powerups = pygame.sprite.Group()

    font = pygame.font.SysFont(None, 36)
    score = 0

    enemy_spawn_event = pygame.USEREVENT + 1
    bullet_spawn_event = pygame.USEREVENT + 2
    powerup_spawn_event = pygame.USEREVENT + 3
    pygame.time.set_timer(enemy_spawn_event, 1000)
    pygame.time.set_timer(bullet_spawn_event, 500)
    pygame.time.set_timer(powerup_spawn_event, 5000)

    enemy_spawn_delay = 1000
    bullet_spawn_delay = 500
    paused = False


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                paused = not paused
            elif not paused and event.type == enemy_spawn_event:
                edge = random.choice(["top", "bottom", "left", "right"])
                if edge == "top":
                    position = (
                        random.randint(0, screen.get_width()),
                        -20,
                    )
                elif edge == "bottom":
                    position = (
                        random.randint(0, screen.get_width()),
                        screen.get_height() + 20,
                    )
                elif edge == "left":
                    position = (
                        -20,
                        random.randint(0, screen.get_height()),
                    )
                else:
                    position = (
                        screen.get_width() + 20,
                        random.randint(0, screen.get_height()),
                    )
                if score >= 40 and random.random() < 0.1:
                    enemies.add(BossEnemy(position))
                elif score >= 20 and random.random() < 0.2:
                    enemies.add(StrongEnemy(position))
                elif score >= 10 and random.random() < 0.3:
                    enemies.add(FastEnemy(position))
                else:
                    enemies.add(Enemy(position))
            elif not paused and event.type == bullet_spawn_event:
                bullet_speed = 15 if player.bullet_speed_timer > 0 else 10
                bullet_kwargs = {"piercing": player.pierce_timer > 0, "speed": bullet_speed}
                direction = (0, -1)
                if player.homing_timer > 0 and len(enemies) > 0:
                    player_pos = pygame.math.Vector2(player.rect.center)
                    nearest = min(
                        enemies,
                        key=lambda e: pygame.math.Vector2(e.rect.center).distance_to(player_pos),
                    )
                    vec = pygame.math.Vector2(nearest.rect.center) - player_pos
                    if vec.length() != 0:
                        direction = vec.normalize()
                if player.triple_shot_timer > 0:
                    offsets = [-15, 0, 15]
                    for dx in offsets:
                        bullets.add(
                            Bullet(
                                (player.rect.centerx + dx, player.rect.centery),
                                direction=direction,
                                **bullet_kwargs,
                            )
                        )
                else:
                    bullets.add(Bullet(player.rect.center, direction=direction, **bullet_kwargs))

            elif not paused and event.type == powerup_spawn_event:
                position = (
                    random.randint(20, screen.get_width() - 20),
                    random.randint(20, screen.get_height() - 20),
                )
                roll = random.random()
                if roll < 0.2:
                    powerups.add(PowerUp(position))
                elif roll < 0.4:
                    powerups.add(ShieldPowerUp(position))
                elif roll < 0.6:
                    powerups.add(SpeedPowerUp(position))
                elif roll < 0.8:
                    powerups.add(TripleShotPowerUp(position))
                elif roll < 0.9:
                    powerups.add(FreezePowerUp(position))
                elif roll < 0.95:
                    powerups.add(PiercePowerUp(position))
                elif roll < 0.97:
                    powerups.add(RapidFirePowerUp(position))
                elif roll < 0.98:
                    powerups.add(MaxHealthPowerUp(position))
                else:
                    powerups.add(HomingPowerUp(position))


        screen.fill((0, 0, 0))
        if not paused:
            freeze_factor = 0.5 if player.freeze_timer > 0 else 1
            player_group.update()
            enemies.update(player.rect.center, freeze_factor)
            bullets.update()
            powerups.update()

        if not paused:
            kills = handle_bullet_enemy_collisions(bullets, enemies)
            score += kills
            if kills > 0 and score % 5 == 0:
                enemy_spawn_delay = max(200, enemy_spawn_delay - 100)
                pygame.time.set_timer(enemy_spawn_event, enemy_spawn_delay)
                if score >= 30:
                    bullet_spawn_delay = max(200, bullet_spawn_delay - 50)
                    pygame.time.set_timer(bullet_spawn_event, bullet_spawn_delay)

            if handle_player_enemy_collisions(player, enemies) and player.health <= 0:
                running = False
            handle_player_powerup_collisions(player, powerups)

        player_group.draw(screen)
        enemies.draw(screen)
        bullets.draw(screen)
        powerups.draw(screen)

        score_surf = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_surf, (10, 10))
        health_surf = font.render(f"Health: {player.health}", True, (255, 255, 255))
        screen.blit(health_surf, (10, 40))
        if player.shield_timer > 0:
            shield_surf = font.render(
                f"Shield: {player.shield_timer // 60}", True, (0, 255, 255)
            )
            screen.blit(shield_surf, (10, 70))
        if player.speed_timer > 0:
            speed_surf = font.render(
                f"Speed: {player.speed_timer // 60}", True, (255, 165, 0)
            )
            screen.blit(speed_surf, (10, 100))
        if player.freeze_timer > 0:
            freeze_surf = font.render(
                f"Freeze: {player.freeze_timer // 60}", True, (173, 216, 230)
            )
            screen.blit(freeze_surf, (10, 130))
        if player.pierce_timer > 0:
            pierce_surf = font.render(
                f"Pierce: {player.pierce_timer // 60}", True, (138, 43, 226)
            )
            screen.blit(pierce_surf, (10, 160))
        if player.homing_timer > 0:
            homing_surf = font.render(
                f"Homing: {player.homing_timer // 60}", True, (255, 215, 0)
            )
            screen.blit(homing_surf, (10, 190))
        if player.bullet_speed_timer > 0:
            rapid_surf = font.render(
                f"Rapid: {player.bullet_speed_timer // 60}", True, (192, 192, 192)
            )
            screen.blit(rapid_surf, (10, 220))



        if paused:
            pause_surf = font.render("Paused", True, (255, 255, 255))
            rect = pause_surf.get_rect(center=screen.get_rect().center)
            screen.blit(pause_surf, rect)

        pygame.display.flip()
        clock.tick(60)

    print(f"Game over! Score: {score}")
    pygame.quit()


if __name__ == "__main__":
    main()

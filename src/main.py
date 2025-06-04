import random
import pygame
from game.player import Player
from game.enemy import Enemy
from game.bullet import Bullet
from game.utils import (
    handle_bullet_enemy_collisions,
    handle_player_enemy_collisions,
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

    font = pygame.font.SysFont(None, 36)
    score = 0

    enemy_spawn_event = pygame.USEREVENT + 1
    bullet_spawn_event = pygame.USEREVENT + 2
    pygame.time.set_timer(enemy_spawn_event, 1000)
    pygame.time.set_timer(bullet_spawn_event, 500)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == enemy_spawn_event:
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
                enemies.add(Enemy(position))
            elif event.type == bullet_spawn_event:
                bullets.add(Bullet(player.rect.center))

        screen.fill((0, 0, 0))
        player_group.update()
        enemies.update(player.rect.center)
        bullets.update()

        score += handle_bullet_enemy_collisions(bullets, enemies)

        if handle_player_enemy_collisions(player, enemies) and player.health <= 0:
            running = False

        player_group.draw(screen)
        enemies.draw(screen)
        bullets.draw(screen)

        score_surf = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_surf, (10, 10))
        health_surf = font.render(f"Health: {player.health}", True, (255, 255, 255))
        screen.blit(health_surf, (10, 40))

        pygame.display.flip()
        clock.tick(60)

    print(f"Game over! Score: {score}")
    pygame.quit()


if __name__ == "__main__":
    main()

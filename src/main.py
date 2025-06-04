import random
import pygame
from game.player import Player
from game.enemy import Enemy
from game.bullet import Bullet


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Vampire Survivor")
    clock = pygame.time.Clock()
    player = Player()
    player_group = pygame.sprite.GroupSingle(player)
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

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
                position = (
                    random.randint(0, screen.get_width()),
                    random.randint(0, screen.get_height()),
                )
                enemies.add(Enemy(position))
            elif event.type == bullet_spawn_event:
                bullets.add(Bullet(player.rect.center))

        screen.fill((0, 0, 0))
        player_group.update()
        enemies.update(player.rect.center)
        bullets.update()

        pygame.sprite.groupcollide(bullets, enemies, True, True)

        if pygame.sprite.spritecollide(player, enemies, False):
            running = False

        player_group.draw(screen)
        enemies.draw(screen)
        bullets.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()

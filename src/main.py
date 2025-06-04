import random
import pygame
from game.enemy import Enemy
from game.player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Vampire Survivor")
    clock = pygame.time.Clock()
    player = Player()
    enemies = pygame.sprite.Group()
    SPAWN_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWN_EVENT, 1000)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == SPAWN_EVENT:
                position = (random.randint(0, 800), random.randint(0, 600))
                enemies.add(Enemy(position))

        screen.fill((0, 0, 0))
        player.update()
        enemies.update(player.rect.center)
        player.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)

        if pygame.sprite.spritecollideany(player, enemies):
            running = False
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()

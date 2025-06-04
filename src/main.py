import random
import pygame

from game.player import Player
from game.enemy import Enemy
from game.constants import SCREEN_WIDTH, SCREEN_HEIGHT


def spawn_enemy():
    side = random.choice(['left', 'right', 'top', 'bottom'])
    if side == 'left':
        return Enemy((0, random.randint(0, SCREEN_HEIGHT)))
    if side == 'right':
        return Enemy((SCREEN_WIDTH, random.randint(0, SCREEN_HEIGHT)))
    if side == 'top':
        return Enemy((random.randint(0, SCREEN_WIDTH), 0))
    return Enemy((random.randint(0, SCREEN_WIDTH), SCREEN_HEIGHT))


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Vampire Survivor")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 24)

    player = Player()
    enemies = pygame.sprite.Group()
    score = 0

    SPAWN_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWN_EVENT, 1000)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == SPAWN_EVENT:
                enemies.add(spawn_enemy())

        player.update()
        enemies.update(player.rect.center)

        # bullet vs enemy collisions
        hits = pygame.sprite.groupcollide(player.bullets, enemies, True, True)
        score += len(hits)

        # enemy vs player collisions
        if pygame.sprite.spritecollideany(player, enemies):
            for enemy in pygame.sprite.spritecollide(player, enemies, True):
                player.health -= 10
            if player.health <= 0:
                running = False

        screen.fill((0, 0, 0))
        enemies.draw(screen)
        player.draw(screen)

        hud = font.render(f"Health: {player.health}  Score: {score}", True, (255, 255, 255))
        screen.blit(hud, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

os.environ["SDL_VIDEODRIVER"] = "dummy"
import pygame
pygame.init()

from game.player import Player
from game.enemy import Enemy
from game.bullet import Bullet


def test_player_has_health():
    player = Player()
    assert player.health == 100


def test_bullet_hits_enemy():
    player = Player()
    enemy = Enemy((player.rect.centerx + 60, player.rect.centery))
    bullet = Bullet(player.rect.center, (1, 0))
    collided = False
    for _ in range(20):
        bullet.update()
        enemy.update(player.rect.center)
        if pygame.sprite.collide_rect(bullet, enemy):
            collided = True
            break
    assert collided

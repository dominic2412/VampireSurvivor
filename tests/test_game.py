import os
import sys
os.environ['SDL_VIDEODRIVER'] = 'dummy'
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
import pygame
pygame.init()

from game.bullet import Bullet
from game.enemy import Enemy, FastEnemy
from game.player import Player
from game.powerup import PowerUp
from game.utils import (
    handle_bullet_enemy_collisions,
    handle_player_enemy_collisions,
    handle_player_powerup_collisions,
)


def test_bullet_moves_up():
    b = Bullet((10, 10), speed=5)
    initial_y = b.rect.y
    b.update()
    assert b.rect.y == initial_y - 5


def test_enemy_moves_toward_target():
    e = Enemy((0, 0), speed=2)
    e.update((3, 0))
    assert e.rect.centerx > 0


def test_fast_enemy_moves_faster():
    e = FastEnemy((0, 0), speed=4)
    e.update((8, 0))
    assert e.rect.centerx > 0
    # With double speed, it should move at least 3 pixels on first update
    assert e.rect.centerx >= 3


def test_collision_returns_score_increment():
    bullets = pygame.sprite.Group(Bullet((0, 0)))
    enemies = pygame.sprite.Group(Enemy((0, 0)))
    killed = handle_bullet_enemy_collisions(bullets, enemies)
    assert killed == 1


def test_player_takes_damage_on_collision():
    player = Player()
    enemies = pygame.sprite.Group(Enemy(player.rect.center))
    collided = handle_player_enemy_collisions(player, enemies)
    assert collided
    assert player.health == 2


def test_player_collects_powerup():
    player = Player(health=1)
    powerups = pygame.sprite.Group(PowerUp(player.rect.center))
    collided = handle_player_powerup_collisions(player, powerups)
    assert collided
    assert player.health == 2


pygame.quit()

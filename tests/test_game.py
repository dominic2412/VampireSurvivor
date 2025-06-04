import os
import sys
os.environ['SDL_VIDEODRIVER'] = 'dummy'
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
import pygame
pygame.init()

from game.bullet import Bullet
from game.enemy import Enemy
from game.utils import handle_bullet_enemy_collisions


def test_bullet_moves_up():
    b = Bullet((10, 10), speed=5)
    initial_y = b.rect.y
    b.update()
    assert b.rect.y == initial_y - 5


def test_enemy_moves_toward_target():
    e = Enemy((0, 0), speed=2)
    e.update((3, 0))
    assert e.rect.centerx > 0


def test_collision_returns_score_increment():
    bullets = pygame.sprite.Group(Bullet((0, 0)))
    enemies = pygame.sprite.Group(Enemy((0, 0)))
    killed = handle_bullet_enemy_collisions(bullets, enemies)
    assert killed == 1


pygame.quit()

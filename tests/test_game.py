import os
import sys
os.environ['SDL_VIDEODRIVER'] = 'dummy'
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
import pygame
pygame.init()

from game.bullet import Bullet
from game.enemy import Enemy


def test_bullet_moves_up():
    b = Bullet((10, 10), speed=5)
    initial_y = b.rect.y
    b.update()
    assert b.rect.y == initial_y - 5


def test_enemy_moves_toward_target():
    e = Enemy((0, 0), speed=2)
    e.update((3, 0))
    assert e.rect.centerx > 0

pygame.quit()

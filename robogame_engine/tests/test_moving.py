# -*- coding: utf-8 -*-
import unittest
from robogame_engine import Scene, GameObject
from robogame_engine.geometry import Point


class TestMoving(unittest.TestCase):

    def setUp(self):
        self.scene = Scene(field=(100, 100))

    def test_move_at(self):
        obj = GameObject(pos=Point(x=10, y=10))
        obj.move_at(target=Point(x=10, y=300), speed=2)
        for i in range(5):
            self.scene.game_step()
        self.assertEqual(obj.y, 20)

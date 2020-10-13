from light import Light
from color import Color
from point import Point
import unittest

class TestLight(unittest.TestCase):
    def test_light1(self):
        light = Light(intensity=Color(1, 1, 1), position=Point(0, 0, 0))
        self.assertTrue(Point(0, 0, 0).equals(light.position))
        self.assertTrue(Color(1, 1, 1).equals(light.intensity))
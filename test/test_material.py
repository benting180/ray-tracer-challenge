from material import Material
from color import Color
from point import Point
from vector import Vector
from light import Light
import unittest
from math import sqrt

class TestMaterial(unittest.TestCase):
    def test_material1(self):
        m = Material()
        self.assertTrue(Color(1, 1, 1).equals(m.color))
        self.assertEqual(0.1, m.ambient)
        self.assertEqual(0.9, m.diffuse)
        self.assertEqual(0.9, m.specular)
        self.assertEqual(200.0, m.shininess)
    
    def test_material2(self):
        position = Point(0, 0, 0)
        m = Material()

        eyev = Vector(0, 0, -1)
        normalv = Vector(0, 0, -1)
        light = Light(Point(0, 0, -10), Color(1, 1, 1))
        in_shadow = False
        result = m.lighting(light, position, eyev, normalv, in_shadow)
        self.assertTrue(Color(1.9, 1.9, 1.9).equals(result))

    def test_material3(self):
        position = Point(0, 0, 0)
        m = Material()

        eyev = Vector(0, sqrt(2)/2, -sqrt(2)/2)
        normalv = Vector(0, 0, -1)
        light = Light(Point(0, 0, -10), Color(1, 1, 1))
        in_shadow = False
        result = m.lighting(light, position, eyev, normalv, in_shadow)
        self.assertTrue(Color(1.0, 1.0, 1.0).equals(result))
    
    def test_material4(self):
        position = Point(0, 0, 0)
        m = Material()

        eyev = Vector(0, 0, -1)
        normalv = Vector(0, 0, -1)
        light = Light(Point(0, 10, -10), Color(1, 1, 1))
        in_shadow = False
        result = m.lighting(light, position, eyev, normalv, in_shadow)
        self.assertTrue(Color(0.7364, 0.7364, 0.7364).equals(result))
    
    def test_material5(self):
        position = Point(0, 0, 0)
        m = Material()

        eyev = Vector(0, -sqrt(2)/2, -sqrt(2)/2)
        normalv = Vector(0, 0, -1)
        light = Light(Point(0, 10, -10), Color(1, 1, 1))
        in_shadow = False
        result = m.lighting(light, position, eyev, normalv, in_shadow)
        self.assertTrue(Color(1.6364, 1.6364, 1.6364).equals(result))
    
    def test_material6(self):
        position = Point(0, 0, 0)
        m = Material()

        eyev = Vector(0, 0, -1)
        normalv = Vector(0, 0, -1)
        light = Light(Point(0, 0, 10), Color(1, 1, 1))
        in_shadow = False
        result = m.lighting(light, position, eyev, normalv, in_shadow)
        self.assertTrue(Color(0.1, 0.1, 0.1).equals(result))

    def test_shadow7(self):
        eyev = Vector(0, 0, -1)
        normalv = Vector(0, 0, -1)
        light = Light(Point(0, 0, -10), Color(1, 1, 1))
        in_shadow = True
        m = Material()
        result = m.lighting(light, Point(0, 0, 0), eyev, normalv, in_shadow)
        self.assertTrue(result.equals(Color(0.1, 0.1, 0.1)))
        
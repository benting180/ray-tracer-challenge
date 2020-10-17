from material import Material
from color import Color
from point import Point
from vector import Vector
from light import Light
import unittest
from math import sqrt
from pattern import StripePattern
from sphere import Sphere

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
        result = m.lighting(Sphere(), light, position, eyev, normalv, in_shadow)
        self.assertTrue(Color(1.9, 1.9, 1.9).equals(result))

    def test_material3(self):
        position = Point(0, 0, 0)
        m = Material()

        eyev = Vector(0, sqrt(2)/2, -sqrt(2)/2)
        normalv = Vector(0, 0, -1)
        light = Light(Point(0, 0, -10), Color(1, 1, 1))
        in_shadow = False
        result = m.lighting(Sphere(), light, position, eyev, normalv, in_shadow)
        self.assertTrue(Color(1.0, 1.0, 1.0).equals(result))
    
    def test_material4(self):
        position = Point(0, 0, 0)
        m = Material()

        eyev = Vector(0, 0, -1)
        normalv = Vector(0, 0, -1)
        light = Light(Point(0, 10, -10), Color(1, 1, 1))
        in_shadow = False
        result = m.lighting(Sphere(), light, position, eyev, normalv, in_shadow)
        self.assertTrue(Color(0.7364, 0.7364, 0.7364).equals(result))
    
    def test_material5(self):
        position = Point(0, 0, 0)
        m = Material()

        eyev = Vector(0, -sqrt(2)/2, -sqrt(2)/2)
        normalv = Vector(0, 0, -1)
        light = Light(Point(0, 10, -10), Color(1, 1, 1))
        in_shadow = False
        result = m.lighting(Sphere(), light, position, eyev, normalv, in_shadow)
        self.assertTrue(Color(1.6364, 1.6364, 1.6364).equals(result))
    
    def test_material6(self):
        position = Point(0, 0, 0)
        m = Material()

        eyev = Vector(0, 0, -1)
        normalv = Vector(0, 0, -1)
        light = Light(Point(0, 0, 10), Color(1, 1, 1))
        in_shadow = False
        result = m.lighting(Sphere(), light, position, eyev, normalv, in_shadow)
        self.assertTrue(Color(0.1, 0.1, 0.1).equals(result))

    def test_shadow7(self):
        eyev = Vector(0, 0, -1)
        normalv = Vector(0, 0, -1)
        light = Light(Point(0, 0, -10), Color(1, 1, 1))
        in_shadow = True
        m = Material()
        result = m.lighting(Sphere(), light, Point(0, 0, 0), eyev, normalv, in_shadow)
        self.assertTrue(result.equals(Color(0.1, 0.1, 0.1)))
    
    def test_lighting_with_a_pattern_applied(self):
        sp = StripePattern(Color(1,1,1), Color(0,0,0))
        m = Material()
        m.pattern = sp
        m.ambient = 1
        m.diffuse = 0
        m.specular = 0
        eyev = Vector(0, 0, -1)
        normalv = Vector(0, 0, -1)
        light = Light(Point(0, 0, -10), Color(1, 1, 1))
        c1 = m.lighting(Sphere(), light, Point(0.9, 0, 0), eyev, normalv, False)
        c2 = m.lighting(Sphere(), light, Point(1.1, 0, 0), eyev, normalv, False)
        self.assertTrue(c1.equals(Color(1, 1, 1)))
        self.assertTrue(c2.equals(Color(0, 0, 0)))
        
import unittest
from plane import Plane
import matrix
from matrix import Matrix
from point import Point
from vector import Vector
from transform import translate, scale, rotate_z
from ray import Ray
from math import sqrt, pi
from material import Material
from shape import Shape

class TestPlane(unittest.TestCase):
    def test_normal1(self):
        p = Plane()
        n1 = p.local_normal_at(Point(0, 0, 0))
        n2 = p.local_normal_at(Point(10, 0, -10))
        n3 = p.local_normal_at(Point(-5, 0, 150))
        self.assertTrue(n1.equals(Vector(0, 1, 0)))
        self.assertTrue(n2.equals(Vector(0, 1, 0)))
        self.assertTrue(n3.equals(Vector(0, 1, 0)))

    def test_intersect1(self):
        p = Plane()
        r = Ray(Point(0, 10, 0), Vector(0, 0, 1))
        xs = p.local_intersect(r)
        self.assertEqual(0, xs.count)

    def test_intersect2(self):
        p = Plane()
        r = Ray(Point(0, 0, 0), Vector(0, 0, 1))
        xs = p.local_intersect(r)
        self.assertEqual(0, xs.count)
    
    def test_intersect3(self):
        p = Plane()
        r = Ray(Point(0, 1, 0), Vector(0, -1, 1))
        xs = p.local_intersect(r)
        self.assertEqual(1, xs.count)
        self.assertEqual(1, xs[0].t)
        self.assertEqual(p, xs[0].obj)
    
    def test_intersect4(self):
        p = Plane()
        r = Ray(Point(0, -1, 0), Vector(0, 1, 1))
        xs = p.local_intersect(r)
        self.assertEqual(1, xs.count)
        self.assertEqual(1, xs[0].t)
        self.assertEqual(p, xs[0].obj)


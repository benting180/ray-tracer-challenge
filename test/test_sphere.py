import unittest
from sphere import Sphere
import matrix
from matrix import Matrix
from point import Point
from vector import Vector
from transform import translate, scale
from ray import Ray

class test_sphere(unittest.TestCase):
    def test_transform1(self):
        s = Sphere()
        I = Matrix([[1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])
        self.assertTrue(matrix.equals(s.transform, I))

    def test_transform2(self):
        s = Sphere()
        t = translate(2, 3, 4)
        s.set_transform(t)
        self.assertTrue(matrix.equals(s.transform, t))

    def test_transform2(self):
        r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
        s = Sphere()
        s.set_transform(scale(2, 2, 2))
        xs = s.intersect(r)

        self.assertEqual(xs.count, 2)
        self.assertTrue(xs[0].t, 3)
        self.assertTrue(xs[1].t, 7)

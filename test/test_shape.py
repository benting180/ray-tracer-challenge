import unittest
import matrix
from matrix import Matrix
from point import Point
from vector import Vector
from transform import translate, scale, rotate_z
from ray import Ray
from math import sqrt, pi
from material import Material
from shape import Shape, TestShape


class test_shape(unittest.TestCase):
    def test_transform1(self):
        s = TestShape()
        I = Matrix([[1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])
        self.assertTrue(matrix.equals(s.transform, I))

    def test_transform2(self):
        s = TestShape()
        t = translate(2, 3, 4)
        s.set_transform(t)
        self.assertTrue(matrix.equals(s.transform, t))

    def test_material1(self):
        s = TestShape()
        m = s.material
        self.assertTrue(Material()==m)
    
    def test_material2(self):
        s = TestShape()
        m = s.material
        m.ambient = 1
        s.material = m
        self.assertTrue(s.material==m)


    def test_intersect1(self):
        r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
        s = TestShape()
        s.set_transform(scale(2, 2, 2))
        xs = s.intersect(r)
        self.assertTrue(s.saved_ray.origin.equals(Point(0, 0, -2.5)))
        self.assertTrue(s.saved_ray.direction.equals(Vector(0, 0, 0.5)))
    
    def test_intersect2(self):
        r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
        s = TestShape()
        s.set_transform(translate(5, 0, 0))
        xs = s.intersect(r)
        self.assertTrue(s.saved_ray.origin.equals(Point(-5, 0, -5)))
        self.assertTrue(s.saved_ray.direction.equals(Vector(0, 0, 1)))

    
    def test_normal1(self):
        s = TestShape()
        s.set_transform(translate(0, 1, 0))
        n = s.normal_at(Point(0, 1.70711, -0.70711))
        self.assertTrue(n.equals(Vector(0, 0.70711, -0.70711)))
    
    def test_normal2(self):
        s = TestShape()
        s.set_transform(scale(1, 0.5, 1)*rotate_z(pi/5))
        n = s.normal_at(Point(0, sqrt(2)/2, -sqrt(2)/2))
        self.assertTrue(n.equals(Vector(0, 0.97014, -0.24254)))
    



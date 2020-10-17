import unittest
from sphere import Sphere
import matrix
from matrix import Matrix
from point import Point
from vector import Vector
from transform import translate, scale, rotate_z
from ray import Ray
from math import sqrt, pi
from material import Material
from shape import Shape

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
    
    def test_normal1(self):
        s = Sphere()
        n = s.normal_at(Point(1, 0, 0))
        self.assertTrue(n.equals(Vector(1, 0, 0)))
    
    def test_normal2(self):
        s = Sphere()
        n = s.normal_at(Point(0, 1, 0))
        self.assertTrue(n.equals(Vector(0, 1, 0)))
    
    def test_normal3(self):
        s = Sphere()
        n = s.normal_at(Point(0, 0, 1))
        self.assertTrue(n.equals(Vector(0, 0, 1)))
        
    def test_normal4(self):
        s = Sphere()
        n = s.normal_at(Point(sqrt(3)/3, sqrt(3)/3, sqrt(3)/3))
        self.assertTrue(n.equals(Vector(sqrt(3)/3, sqrt(3)/3, sqrt(3)/3)))
    
    def test_normal5(self):
        s = Sphere()
        s.set_transform(translate(0, 1, 0))
        n = s.normal_at(Point(0, 1.70711, -0.70711))
        self.assertTrue(n.equals(Vector(0, 0.70711, -0.70711)))
    
    def test_normal6(self):
        s = Sphere()
        s.set_transform(scale(1, 0.5, 1)*rotate_z(pi/5))
        n = s.normal_at(Point(0, sqrt(2)/2, -sqrt(2)/2))
        self.assertTrue(n.equals(Vector(0, 0.97014, -0.24254)))

    def test_material1(self):
        s = Sphere()
        m = s.material
        self.assertTrue(Material()==m)
    
    def test_material2(self):
        s = Sphere()
        m = s.material
        m.ambient = 1
        s.material = m
        self.assertTrue(s.material==m)

    def test_type1(self):
        s = Sphere()
        self.assertEqual(s.parent, Shape)
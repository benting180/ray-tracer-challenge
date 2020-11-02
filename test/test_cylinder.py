import unittest
from sphere import Sphere, GlassSphere
import matrix

from matrix import Matrix, I
from point import Point
from vector import Vector
from transform import translate, scale, rotate_z
from ray import Ray
from math import sqrt, pi
from material import Material
from shape import Shape
from misc import equals
from cylinder import Cylinder

class TestCylinder(unittest.TestCase):
    def test_a_ray_misses_a_cylinder1(self):
        cyl = Cylinder()
        direction = Vector(0, 1, 0).normalize()
        r = Ray(Point(1, 0, 0), direction)
        xs = cyl.local_intersect(r)
        self.assertEqual(0, xs.count)

    def test_a_ray_misses_a_cylinder2(self):
        cyl = Cylinder()
        direction = Vector(0, 1, 0).normalize()
        r = Ray(Point(0, 0, 0), direction)
        xs = cyl.local_intersect(r)
        self.assertEqual(0, xs.count)

    def test_a_ray_misses_a_cylinder3(self):
        cyl = Cylinder()
        direction = Vector(1, 1, 1).normalize()
        r = Ray(Point(0, 0, -5), direction)
        xs = cyl.local_intersect(r)
        self.assertEqual(0, xs.count)

    
    def test_a_ray_strikes_a_cylinder1(self):
        cyl = Cylinder()
        direction = Vector(0, 0, 1)  .normalize()
        r = Ray(Point(1, 0, -5), direction)
        xs = cyl.local_intersect(r)
        self.assertEqual(2, xs.count)
        self.assertTrue(equals(5.0, xs[0].t))
        self.assertTrue(equals(5.0, xs[1].t))
        
    def test_a_ray_strikes_a_cylinder2(self):
        cyl = Cylinder()
        direction = Vector(0, 0, 1)  .normalize()
        r = Ray(Point(0, 0, -5), direction)
        xs = cyl.local_intersect(r)
        self.assertEqual(2, xs.count)
        self.assertTrue(equals(4.0, xs[0].t))
        self.assertTrue(equals(6.0, xs[1].t))
        
    def test_a_ray_strikes_a_cylinder3(self):
        cyl = Cylinder()
        direction = Vector(0.1, 1, 1).normalize()
        r = Ray(Point(0.5, 0, -5), direction)
        xs = cyl.local_intersect(r)
        self.assertEqual(2, xs.count)
        self.assertTrue(equals(6.80798, xs[0].t))
        self.assertTrue(equals(7.08872, xs[1].t))
        
         
    def test_normal_vector_on_a_cylinder(self):
        cyl = Cylinder()
        n = cyl.local_normal_at(Point(1, 0, 0) )
        self.assertTrue(Vector(1, 0, 0) == n)

    def test_normal_vector_on_a_cylinder(self):
        cyl = Cylinder()
        n = cyl.local_normal_at(Point(0, 5, -1))
        self.assertTrue(Vector(0, 0, -1) == n)

    def test_normal_vector_on_a_cylinder(self):
        cyl = Cylinder()
        n = cyl.local_normal_at(Point(0, -2, 1))
        self.assertTrue(Vector(0, 0, 1) == n)

    def test_normal_vector_on_a_cylinder(self):
        cyl = Cylinder()
        n = cyl.local_normal_at(Point(-1, 1, 0))
        self.assertTrue(Vector(-1, 0, 0) == n)

    def test_default_minimum_and_maximum_for_a_cylinder(self):
        cyl = Cylinder()
        self.assertEqual(cyl.minimum, float('-inf'))
        self.assertEqual(cyl.maximum, float('inf'))
    
    def test_intersecting_a_constrained_cylinder(self):
        cyl = cylinder(1, 2)
            


    def test_intersecting_a_constrained_cylinder(self):
        cyl = Cylinder(1, 2)
        direction = Vector(0.1, 1, 0)
        r = Ray(Point(0,1.5, 0), direction)
        xs = cyl.local_intersect(r)
        self.assertEqual(xs.count, 0)
        
        
    def test_intersecting_a_constrained_cylinder(self):
        cyl = Cylinder(1, 2)
        direction = Vector(0, 0, 1)
        r = Ray(Point(0,3, -5), direction)
        xs = cyl.local_intersect(r)
        self.assertEqual(xs.count, 0)
        
        
    def test_intersecting_a_constrained_cylinder(self):
        cyl = Cylinder(1, 2)
        direction = Vector(0, 0, 1)
        r = Ray(Point(0,0, -5), direction)
        xs = cyl.local_intersect(r)
        self.assertEqual(xs.count, 0)
        
        
    def test_intersecting_a_constrained_cylinder(self):
        cyl = Cylinder(1, 2)
        direction = Vector(0, 0, 1)
        r = Ray(Point(0,2, -5), direction)
        xs = cyl.local_intersect(r)
        self.assertEqual(xs.count, 0)
        
        
    def test_intersecting_a_constrained_cylinder(self):
        cyl = Cylinder(1, 2)
        direction = Vector(0, 0, 1)
        r = Ray(Point(0,1, -5), direction)
        xs = cyl.local_intersect(r)
        self.assertEqual(xs.count, 0)
        
        
    def test_intersecting_a_constrained_cylinder(self):
        cyl = Cylinder(1, 2)
        direction = Vector(0, 0, 1)
        r = Ray(Point(0,1.5, -2), direction)
        xs = cyl.local_intersect(r)
        self.assertEqual(xs.count, 2)
        
        















































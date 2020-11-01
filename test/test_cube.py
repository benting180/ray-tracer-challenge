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
from cube import Cube

class TestCube(unittest.TestCase):
    def test_ray_intersects_cube_1(self):
        c = Cube()
        r = Ray(Point(5, 0.5, 0), Vector(-1, 0, 0))
        xs = c.local_intersect(r)
        self.assertTrue(equals(xs.count, 2))
        self.assertTrue(equals(4, xs[0].t))
        self.assertTrue(equals(6, xs[1].t))
    def test_ray_intersects_cube_2(self):
        c = Cube()
        r = Ray(Point(-5, 0.5, 0), Vector(1, 0, 0))
        xs = c.local_intersect(r)
        self.assertTrue(equals(xs.count, 2))
        self.assertTrue(equals(4, xs[0].t))
        self.assertTrue(equals(6, xs[1].t))
    def test_ray_intersects_cube_3(self):
        c = Cube()
        r = Ray(Point(0.5, 5, 0), Vector(0, -1, 0))
        xs = c.local_intersect(r)
        self.assertTrue(equals(xs.count, 2))
        self.assertTrue(equals(4, xs[0].t))
        self.assertTrue(equals(6, xs[1].t))
    def test_ray_intersects_cube_4(self):
        c = Cube()
        r = Ray(Point(0.5, -5, 0), Vector(0, 1, 0))
        xs = c.local_intersect(r)
        self.assertTrue(equals(xs.count, 2))
        self.assertTrue(equals(4, xs[0].t))
        self.assertTrue(equals(6, xs[1].t))
    def test_ray_intersects_cube_5(self):
        c = Cube()
        r = Ray(Point(0.5, 0, 5), Vector(0, 0, -1))
        xs = c.local_intersect(r)
        self.assertTrue(equals(xs.count, 2))
        self.assertTrue(equals(4, xs[0].t))
        self.assertTrue(equals(6, xs[1].t))
    def test_ray_intersects_cube_6(self):
        c = Cube()
        r = Ray(Point(0.5, 0, -5), Vector(0, 0, 1))
        xs = c.local_intersect(r)
        self.assertTrue(equals(xs.count, 2))
        self.assertTrue(equals(4, xs[0].t))
        self.assertTrue(equals(6, xs[1].t))
    def test_ray_intersects_cube_7(self):
        c = Cube()
        r = Ray(Point(0, 0.5, 0), Vector(0, 0, 1))
        xs = c.local_intersect(r)
        self.assertTrue(equals(xs.count, 2))
        self.assertTrue(equals(-1, xs[0].t))
        self.assertTrue(equals(1, xs[1].t))

    def test_ray_miss_cube1(self):
        c = Cube()
        r = Ray(Point(-2, 0, 0), Vector(0.2673, 0.5345, 0.8018))
        xs = c.local_intersect(r)
        self.assertTrue(equals(0, xs.count))

    def test_ray_miss_cube2(self):
        c = Cube()
        r = Ray(Point(0, -2, 0), Vector(0.8018, 0.2673, 0.5345))
        xs = c.local_intersect(r)
        self.assertTrue(equals(0, xs.count))

    def test_ray_miss_cube3(self):
        c = Cube()
        r = Ray(Point(0, 0, -2), Vector(0.5345, 0.8018, 0.2673))
        xs = c.local_intersect(r)
        self.assertTrue(equals(0, xs.count))

    def test_ray_miss_cube4(self):
        c = Cube()
        r = Ray(Point(2, 0, 2), Vector(0, 0, -1))
        xs = c.local_intersect(r)
        self.assertTrue(equals(0, xs.count))

    def test_ray_miss_cube5(self):
        c = Cube()
        r = Ray(Point(0, 2, 2), Vector(0, -1, 0))
        xs = c.local_intersect(r)
        self.assertTrue(equals(0, xs.count))

    def test_ray_miss_cube6(self):
        c = Cube()
        r = Ray(Point(2, 2, 0), Vector(-1, 0, 0))
        xs = c.local_intersect(r)
        self.assertTrue(equals(0, xs.count))

    def test_normal_on_the_surface_of_cube(self):
        c = Cube()
        p = Point(1, 0.5, -0.8)
        normal = c.local_normal_at(p)
        self.assertTrue(Vector(1, 0, 0) == normal)

    def test_normal_on_the_surface_of_cube(self):
        c = Cube()
        p = Point(-1, -0.2, 0.9)
        normal = c.local_normal_at(p)
        self.assertTrue(Vector(-1, 0, 0) == normal)

    def test_normal_on_the_surface_of_cube(self):
        c = Cube()
        p = Point(-0.4, 1, -0.1)
        normal = c.local_normal_at(p)
        self.assertTrue(Vector(0, 1, 0) == normal)

    def test_normal_on_the_surface_of_cube(self):
        c = Cube()
        p = Point(0.3, -1, -0.7)
        normal = c.local_normal_at(p)
        self.assertTrue(Vector(0, -1, 0) == normal)

    def test_normal_on_the_surface_of_cube(self):
        c = Cube()
        p = Point(-0.6, 0.3, 1)
        normal = c.local_normal_at(p)
        self.assertTrue(Vector(0, 0, 1) == normal)

    def test_normal_on_the_surface_of_cube(self):
        c = Cube()
        p = Point(0.4, 0.4, -1)
        normal = c.local_normal_at(p)
        self.assertTrue(Vector(0, 0, -1) == normal)

    def test_normal_on_the_surface_of_cube(self):
        c = Cube()
        p = Point(1, 1, 1)
        normal = c.local_normal_at(p)
        self.assertTrue(Vector(1, 0, 0) == normal)

    def test_normal_on_the_surface_of_cube(self):
        c = Cube()
        p = Point(-1, -1, -1)
        normal = c.local_normal_at(p)
        self.assertTrue(Vector(-1, 0, 0) == normal)

















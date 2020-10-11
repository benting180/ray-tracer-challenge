import unittest
from base import Base
from point import Point
from vector import Vector
from misc import equals
import matrix
from matrix import Matrix
from ray import Ray
from sphere import Sphere
from intersections import Intersections, Intersection
from transform import translate, scale


class test_ray(unittest.TestCase):
    def test_ray1(self):
        origin = Point(1, 2, 3)
        direction = Vector(4, 5, 6)
        r = Ray(origin, direction)
        self.assertTrue(origin.equals(r.origin))
        self.assertTrue(direction.equals(r.direction))

    def test_ray2(self):
        origin = Point(2, 3, 4)
        direction = Vector(1, 0, 0)
        r = Ray(origin, direction)
        self.assertTrue(Point(2, 3, 4).equals(r.position(0)))
        self.assertTrue(Point(3, 3, 4).equals(r.position(1)))
        self.assertTrue(Point(1, 3, 4).equals(r.position(-1)))
        self.assertTrue(Point(4.5, 3, 4).equals(r.position(2.5)))
    
    def test_intersect1(self):
        origin = Point(0, 0, -5)
        direction = Vector(0, 0, 1)
        r = Ray(origin, direction)
        s = Sphere()
        i1 = Intersection(4, s)
        i2 = Intersection(6, s)
        xs = Intersections([i1, i2])
        self.assertTrue(s.interset(r)==xs)

    def test_intersect2(self):
        origin = Point(0, 1, -5)
        direction = Vector(0, 0, 1)
        r = Ray(origin, direction)
        s = Sphere()
        i1 = Intersection(5, s)
        i2 = Intersection(5, s)
        xs = Intersections([i1, i2])
        self.assertTrue(s.interset(r)==xs)
    
    def test_intersect3(self):
        origin = Point(0, 2, -5)
        direction = Vector(0, 0, 1)
        r = Ray(origin, direction)
        s = Sphere()
        xs = Intersections([])
        self.assertTrue(s.interset(r)==xs)
    
    def test_intersect4(self):
        origin = Point(0, 0, 0)
        direction = Vector(0, 0, 1)
        r = Ray(origin, direction)
        s = Sphere()
        i1 = Intersection(-1, s)
        i2 = Intersection(1, s)
        xs = Intersections([i1, i2])
        self.assertTrue(s.interset(r)==xs)
    
    def test_intersect5(self):
        origin = Point(0, 0, 5)
        direction = Vector(0, 0, 1)
        r = Ray(origin, direction)
        s = Sphere()
        i1 = Intersection(-6, s)
        i2 = Intersection(-4, s)
        xs = Intersections([i1, i2])
        self.assertTrue(s.interset(r)==xs)
        
    def test_transform1(self):
        r = Ray(Point(1, 2, 3), Vector(0, 1, 0))
        m = translate(3, 4, 5)
        r2 = r.transform(m)
        self.assertTrue(r2.origin.equals(Point(4, 6, 8)))
        self.assertTrue(r2.direction.equals(Vector(0, 1, 0)))

    def test_transform2(self):
        r = Ray(Point(1, 2, 3), Vector(0, 1, 0))
        m = scale(2, 3, 4)
        r2 = r.transform(m)
        self.assertTrue(r2.origin.equals(Point(2, 6, 12)))
        self.assertTrue(r2.direction.equals(Vector(0, 3, 0)))

if __name__ == '__main__':
    unittest.main()

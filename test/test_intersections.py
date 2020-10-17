import unittest
from intersections import Intersection, Intersections
from sphere import Sphere
from ray import Ray
from point import Point
from vector import Vector
from misc import EPSILON
from transform import translate

class test_intersections(unittest.TestCase):
    def test_int1(self):
        s = Sphere()
        i = Intersection(3.5, s)
        self.assertEqual(i.t, 3.5)
        self.assertTrue(i.obj==s)
    
    def test_int2(self):
        s = Sphere()
        i1 = Intersection(1, s)
        i2 = Intersection(2, s)
        xs = Intersections([i1, i2])
        self.assertEqual(xs.count, 2)
        self.assertEqual(xs[0].t, 1)
        self.assertEqual(xs[1].t, 2)

    def test_hit1(self):
        s = Sphere()
        i1 = Intersection(1, s)
        i2 = Intersection(2, s)
        xs = Intersections([i1, i2])
        i = xs.hit()
        self.assertTrue(i==i1)

    def test_hit2(self):
        s = Sphere()
        i1 = Intersection(-1, s)
        i2 = Intersection(1, s)
        xs = Intersections([i1, i2])
        i = xs.hit()
        self.assertTrue(i==i2)

    def test_hit3(self):
        s = Sphere()
        i1 = Intersection(-2, s)
        i2 = Intersection(-1, s)
        xs = Intersections([i1, i2])
        i = xs.hit()
        self.assertTrue(i==None)

    def test_hit4(self):
        s = Sphere()
        i1 = Intersection(5, s)
        i2 = Intersection(7, s)
        i3 = Intersection(-3, s)
        i4 = Intersection(2, s)
        xs = Intersections([i1, i2, i3, i4])
        i = xs.hit()
        self.assertTrue(i==i4)
    
    def test_prepare1(self):
        r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
        s = Sphere()
        i = Intersection(4, s)
        comps = i.prepare_computations(r)

        self.assertEqual(i.t, comps.t)
        self.assertTrue(i.obj==comps.obj)
        self.assertTrue(Point(0, 0, -1).equals(comps.point))
        self.assertTrue(Vector(0, 0, -1).equals(comps.eyev))
        self.assertTrue(Vector(0, 0, -1).equals(comps.normalv))

    def test_prepare2(self):
        r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
        s = Sphere()
        i = Intersection(4, s)
        comps = i.prepare_computations(r)
        self.assertFalse(comps.inside)

    def test_prepare3(self):
        r = Ray(Point(0, 0, 0), Vector(0, 0, 1))
        s = Sphere()
        i = Intersection(1, s)
        comps = i.prepare_computations(r)

        self.assertTrue(comps.inside)
        self.assertTrue(Point(0, 0, 1).equals(comps.point))
        self.assertTrue(Vector(0, 0, -1).equals(comps.eyev))
        self.assertTrue(Vector(0, 0, -1).equals(comps.normalv))
    
    def test_offset1(self):
        r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
        shape = Sphere()
        shape.transform = translate(0, 0, 1)
        i = Intersection(5, shape)
        comps = i.prepare_computations(r)
        self.assertTrue(comps.over_point.z < -EPSILON/2)
        self.assertTrue(comps.point.z > comps.over_point.z)

        

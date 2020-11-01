import unittest
from intersections import Intersection, Intersections
from sphere import Sphere, GlassSphere
from ray import Ray
from point import Point
from vector import Vector
from misc import EPSILON, equals
from transform import translate, scale
from world import World
from plane import Plane
from color import Color
from math import sqrt

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

        
    def test_refract1(self):
        A = GlassSphere()
        A.set_transform(scale(2, 2, 2))
        A.material.refractive_index = 1.5

        B = GlassSphere()
        B.set_transform(translate(0, 0, -0.25))
        B.material.refractive_index = 2.0

        C = GlassSphere()
        C.set_transform(translate(0, 0, 0.25))
        C.material.refractive_index = 2.5

        r = Ray(Point(0, 0, -4), Vector(0, 0, 1))

        ls = [
                Intersection(2, A),
                Intersection(2.75, B),
                Intersection(3.25, C),
                Intersection(4.75, B),
                Intersection(5.25, C),
                Intersection(6, A)
            ]
        xs = Intersections(ls)
        
        comps0 = xs[0].prepare_computations(r, xs)
        self.assertEqual(comps0.n1, 1.0)
        self.assertEqual(comps0.n2, 1.5)

        comps1 = xs[1].prepare_computations(r, xs)
        self.assertEqual(comps1.n1, 1.5)
        self.assertEqual(comps1.n2, 2.0)

        comps2 = xs[2].prepare_computations(r, xs)
        self.assertEqual(comps2.n1, 2.0)
        self.assertEqual(comps2.n2, 2.5)

        comps3 = xs[3].prepare_computations(r, xs)
        self.assertEqual(comps3.n1, 2.5)
        self.assertEqual(comps3.n2, 2.5)

        comps4 = xs[4].prepare_computations(r, xs)
        self.assertEqual(comps4.n1, 2.5)
        self.assertEqual(comps4.n2, 1.5)

        comps5 = xs[5].prepare_computations(r, xs)
        self.assertEqual(comps5.n1, 1.5)
        self.assertEqual(comps5.n2, 1.0)

    def test_under_point1(self):
        r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
        shape = GlassSphere()
        shape.set_transform(translate(0, 0, 1))
        i = Intersection(5, shape)
        xs = Intersections([i])
        comps = i.prepare_computations(r, xs)
        # print(comps.normalv)
        # print(comps.point)
        # print(comps.under_point.z)
        self.assertTrue(comps.under_point.z > EPSILON/2)
        self.assertTrue(comps.point.z < comps.under_point.z)

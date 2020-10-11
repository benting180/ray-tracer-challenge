import unittest
from intersections import Intersection, Intersections
from sphere import Sphere
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


from math import sqrt
import unittest
from point import Point
from vector import Vector
from base import Base




class TestPrimitive(unittest.TestCase):
    def test_point(self):
        p = Point(4, -4, 3)
        b = Base(4, -4, 3, 1)
        self.assertTrue(p.equals(b))

    def test_vector(self):
        v = Vector(4, -4, 3)
        b = Base(4, -4, 3, 0)
        self.assertTrue(v.equals(b))

    def test_add1(self):
        a1 = Base(3, -2, 5, 1)
        a2 = Base(-2, 3, 1, 0)
        self.assertTrue(Base(1, 1, 6, 1).equals(a1 + a2))
    
    def test_sub1(self):
        p1 = Point(3, 2, 1)
        p2 = Point(5, 6, 7)
        self.assertTrue(Vector(-2, -4, -6).equals(p1-p2))
    
    def test_sub2(self):
        p = Point(3, 2, 1)
        v = Vector(5, 6, 7)
        self.assertTrue(Point(-2, -4, -6).equals(p-v))

    def test_sub3(self):
        v1 = Vector(3, 2, 1)
        v2 = Vector(5, 6, 7)
        self.assertTrue(Vector(-2, -4, -6).equals(v1 - v2))
    
    def test_neg1(self):
        zero = Vector(0, 0, 0)
        v = Vector(1, -2, 3)
        self.assertTrue(Vector(-1, 2, -3).equals(zero-v))
    
    def test_neg2(self):
        a = Base(1, -2, 3, -4)
        self.assertTrue(-a.equals(a))

    def test_mul1(self):
        a = Base(1, -2, 3, -4)
        self.assertTrue(Base(3.5, -7, 10.5, -14).equals(a*3.5))
    
    def test_mul2(self):
        a = Base(1, -2, 3, -4)
        self.assertTrue(Base(0.5, -1, 1.5, -2).equals(a*0.5))
    
    def test_div(self):
        a = Base(1, -2, 3, -4)
        self.assertTrue(Base(0.5, -1, 1.5, -2).equals(a/2))
    
    def test_mag1(self):
        v = Vector(1, 0, 0)
        self.assertEqual(1, v.mag())
    
    def test_mag2(self):
        v = Vector(0, 1, 0)
        self.assertEqual(1, v.mag())

    def test_mag3(self):
        v = Vector(0, 0, 1)
        self.assertEqual(1, v.mag())
    
    def test_mag4(self):
        v = Vector(1, 2, 3)
        self.assertEqual(sqrt(14), v.mag())
    
    def test_mag5(self):
        v = Vector(-1, -2, -3)
        self.assertEqual(sqrt(14), v.mag())

    def test_nor1(self):
        v = Vector(4, 0, 0)
        self.assertTrue(Vector(1, 0, 0).equals(v.normal()))
    
    def test_nor2(self):
        v = Vector(1, 2, 3)
        self.assertTrue(Vector(1/sqrt(14), 2/sqrt(14), 3/sqrt(14)).equals(v.normal()))
    
    def test_nor3(self):
        v = Vector(1, 2, 3)
        self.assertEqual(1, v.normal().mag())
    
    def test_dot(self):
        a = Vector(1, 2, 3)
        b = Vector(2, 3, 4)
        self.assertTrue(Vector(-1, 2, -1).equals(a.cross(b)))
        self.assertTrue(Vector(1, -2, 1).equals(b.cross(a)))


if __name__ == '__main__':
    unittest.main()
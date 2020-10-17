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
from pattern import StripePattern, TestPattern
from color import Color
from sphere import Sphere
import matrix

class TestPatternClass(unittest.TestCase):
    def test_default(self):
        p = TestPattern()
        I = Matrix([[1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])
        self.assertTrue(matrix.equals(I, p.transform))



    def test_transform1(self):
        p = TestPattern()
        p.set_pattern_transform(translate(1, 2, 3))
        self.assertTrue(matrix.equals(p.transform, translate(1, 2, 3)))


    def test_pattern_with_an_object_transformation(self):
        s = Sphere()
        s.set_transform(scale(2, 2, 2))
        p = TestPattern()
        c = p.stripe_at_object(s, Point(2, 3, 4))
        self.assertTrue(c.equals(Color(1, 1.5, 2)))

    def test_pattern_with_a_pattern_transformation(self):
        s = Sphere()
        p = TestPattern()
        p.set_pattern_transform(scale(2, 2, 2))
        c = p.stripe_at_object(s, Point(2, 3, 4))
        self.assertTrue(c.equals(Color(1, 1.5, 2)))

    def test_pattern_with_both_an_object_and_a_pattern_transformation(self):
        s = Sphere()
        s.set_transform(scale(2, 2, 2))
        p = TestPattern()
        p.set_pattern_transform(translate(0.5, 1, 1.5))
        c = p.stripe_at_object(s, Point(2.5, 3, 3.5))
        self.assertTrue(c.equals(Color(0.75, 0.5, 0.25)))



class TestStripePattern(unittest.TestCase):
    def test_creating_a_stripe_pattern(self):
        black = Color(0, 0, 0)
        white = Color(1, 1, 1)
        p = StripePattern(white, black)
        p.a = white
        p.b = black
    
    def test_a_stripe_pattern_is_constant_in_y(self):
        black = Color(0, 0, 0)
        white = Color(1, 1, 1)
        p = StripePattern(white, black)
        self.assertTrue(white.equals(p.stripe_at(Point(0, 0, 0))))
        self.assertTrue(white.equals(p.stripe_at(Point(0, 1, 0))))
        self.assertTrue(white.equals(p.stripe_at(Point(0, 2, 0))))

    def test_a_stripe_pattern_is_constant_in_z(self):
        black = Color(0, 0, 0)
        white = Color(1, 1, 1) 
        p = StripePattern(white, black)
        self.assertTrue(white.equals(p.stripe_at(Point(0, 0, 0))))
        self.assertTrue(white.equals(p.stripe_at(Point(0, 0, 1))))
        self.assertTrue(white.equals(p.stripe_at(Point(0, 0, 2))))

    def test_a_stripe_pattern_alternates_in_x(self):
        black = Color(0, 0, 0)
        white = Color(1, 1, 1)
        p = StripePattern(white, black)
        self.assertTrue(white.equals(p.stripe_at(Point(0, 0, 0))))
        self.assertTrue(white.equals(p.stripe_at(Point(0.9, 0, 0))))
        self.assertTrue(black.equals(p.stripe_at(Point(1, 0, 0))))
        self.assertTrue(black.equals(p.stripe_at(Point(-0.1, 0, 0))))
        self.assertTrue(black.equals(p.stripe_at(Point(-1, 0, 0))))
        self.assertTrue(white.equals(p.stripe_at(Point(-1.1, 0, 0))))
    
    def test_stripes_with_an_object_transformation(self):
        black = Color(0, 0, 0)
        white = Color(1, 1, 1)
        s = Sphere()
        s.set_transform(scale(2, 2, 2))
        p = StripePattern(white, black)
        c = p.stripe_at_object(s, Point(1.5, 0, 0))
        self.assertTrue(c.equals(white))

    def test_stripes_with_a_pattern_transformation(self):
        black = Color(0, 0, 0)
        white = Color(1, 1, 1)
        s = Sphere()
        p = StripePattern(white, black)
        p.set_pattern_transform(scale(2, 2, 2))
        c = p.stripe_at_object(s, Point(1.5, 0, 0))
        self.assertTrue(c.equals(white))

    def test_stripes_with_both_an_object_and_a_pattern_transformation(self):
        black = Color(0, 0, 0)
        white = Color(1, 1, 1)
        s = Sphere()
        s.set_transform(scale(2, 2, 2))
        p = StripePattern(white, black)
        p.set_pattern_transform(translate(0.5, 0, 0))
        c = p.stripe_at_object(s, Point(2.5, 0, 0))
        self.assertTrue(c.equals(white))
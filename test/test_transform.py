import unittest
from transform import view_transform, scale, translate
from point import Point
from vector import Vector
import matrix
from matrix import Matrix

class TestTransform(unittest.TestCase):
    def test_transform1(self):
        pfrom = Point(0, 0, 0)
        pto = Point(0, 0, -1)
        vup = Vector(0, 1, 0)
        
        t = view_transform(pfrom, pto, vup)
        I = Matrix([[1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]])
        self.assertTrue(matrix.equals(I, t))

    def test_transform2(self):
        pfrom = Point(0, 0, 0)
        pto = Point(0, 0, 1)
        vup = Vector(0, 1, 0)
        
        t = view_transform(pfrom, pto, vup)
        s = scale(-1, 1, -1)
        self.assertTrue(matrix.equals(s, t))

    def test_transform3(self):
        pfrom = Point(0, 0, 8)
        pto = Point(0, 0, 0)
        vup = Vector(0, 1, 0)
        t = view_transform(pfrom, pto, vup)
        self.assertTrue(matrix.equals(translate(0, 0, -8), t))

    def test_transform4(self):
        pfrom = Point(1, 3, 2)
        pto = Point(4, -2, 8)
        vup = Vector(1, 1, 0)
        t = view_transform(pfrom, pto, vup)

        m = Matrix([[-0.50709, 0.50709,  0.67612, -2.36643],
                    [ 0.76772, 0.60609,  0.12122, -2.82843],
                    [-0.35857, 0.59761, -0.71714,  0.00000],
                    [ 0.00000, 0.00000,  0.00000,  1.00000]])

        self.assertTrue(matrix.equals(m, t))

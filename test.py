from math import sqrt
import unittest
from io import StringIO
from base import Base
from point import Point
from vector import Vector
import color
from color import Color
from misc import equals
from canvas import Canvas



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
        self.assertTrue(equals(1, v.mag()))
    
    def test_mag2(self):
        v = Vector(0, 1, 0)
        self.assertTrue(equals(1, v.mag()))

    def test_mag3(self):
        v = Vector(0, 0, 1)
        self.assertTrue(equals(1, v.mag()))
    
    def test_mag4(self):
        v = Vector(1, 2, 3)
        self.assertTrue(equals(sqrt(14), v.mag()))
    
    def test_mag5(self):
        v = Vector(-1, -2, -3)
        self.assertTrue(equals(sqrt(14), v.mag()))

    def test_nor1(self):
        v = Vector(4, 0, 0)
        self.assertTrue(Vector(1, 0, 0).equals(v.normal()))
    
    def test_nor2(self):
        v = Vector(1, 2, 3)
        self.assertTrue(Vector(1/sqrt(14), 2/sqrt(14), 3/sqrt(14)).equals(v.normal()))
    
    def test_nor3(self):
        v = Vector(1, 2, 3)
        self.assertTrue(equals(1, v.normal().mag()))
    
    def test_dot(self):
        a = Vector(1, 2, 3)
        b = Vector(2, 3, 4)
        self.assertTrue(Vector(-1, 2, -1).equals(a.cross(b)))
        self.assertTrue(Vector(1, -2, 1).equals(b.cross(a)))
    
    def test_color1(self):
        c = Color(-0.5, 0.4, 1.7)
        self.assertTrue(equals(c.x, -0.5))
        self.assertTrue(equals(c.y, 0.4))
        self.assertTrue(equals(c.z, 1.7))

    def test_color2(self):
        c1 = Color(0.9, 0.6, 0.75)
        c2 = Color(0.7, 0.1, 0.25)
        c3 = c1+c2
        self.assertTrue(equals(c3.x, 1.6))
        self.assertTrue(equals(c3.y, 0.7))
        self.assertTrue(equals(c3.z, 1))
    
    def test_color3(self):
        c1 = Color(0.9, 0.6, 0.75)
        c2 = Color(0.7, 0.1, 0.25)
        c3 = c1-c2
        self.assertTrue(equals(c3.x, 0.2))
        self.assertTrue(equals(c3.y, 0.5))
        self.assertTrue(equals(c3.z, 0.5))

    def test_color4(self):
        c1 = Color(0.2, 0.3, 0.4)
        c2 = c1*2
        self.assertTrue(equals(c2.x, 0.4))
        self.assertTrue(equals(c2.y, 0.6))
        self.assertTrue(equals(c2.z, 0.8))

    def test_color5(self):
        c1 = Color(1, 0.2, 0.4)
        c2 = Color(0.9, 1, 0.1)
        c3 = color.hadamard_product(c1, c2)
        self.assertTrue(c3.equals(Color(0.9, 0.2, 0.04)))


class TestCanvas(unittest.TestCase):
    def test_create1(self):
        c = Canvas(10, 20)
        self.assertTrue(equals(10, c.width))
        self.assertTrue(equals(20, c.height))
        for i in range(10):
            for j in range(20):
                pixel = c.pixels[j][i]
                self.assertTrue(pixel.equals(Color(0, 0, 0)))
    def test_write(self):
        c = Canvas(10, 20)
        red = Color(1, 0, 0)
        c.write_pixel(2, 3, red)
        self.assertTrue(c.pixel_at(2, 3).equals(red))
    
    def test_ppm1(self):
        return
        # how to unittest file write
        # https://stackoverflow.com/a/3945057
        # outfile = StringIO()
        # c = Canvas(5, 3)
        # c.to_ppm(outfile)
        # outfile.seek(0)
        # contents = outfile.read()
        # self.assertEqual(contents, "P3\n5 3\n255")
    
    def test_ppm2(self):
        outfile = StringIO()
        c = Canvas(5, 3)
        c1 = Color(1.5, 0, 0)
        c2 = Color(0, 0.5, 0)
        c3 = Color(-0.5, 0, 1)
        c.write_pixel(0, 0, c1)
        c.write_pixel(2, 1, c2)
        c.write_pixel(4, 2, c3)

        c.to_ppm(outfile)
        outfile.seek(0)
        contents = outfile.read()
        self.assertEqual(contents, "P3\n5 3\n255\n255 0 0 0 0 0 0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 128 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 0 0 0 0 0 255 \n")
    
        





if __name__ == '__main__':
    unittest.main()
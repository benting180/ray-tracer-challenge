import unittest
from math import pi, sqrt
import matrix
from matrix import Matrix
from camera import Camera
from misc import equals
from transform import translate, rotate_y, view_transform
from point import Point
from vector import Vector
from world import World
from color import Color


class TestCamera(unittest.TestCase):
    def test_camera1(self):
        hsize = 160
        vsize = 120
        field_of_view = pi/2
        c = Camera(hsize, vsize, field_of_view)
        self.assertEqual(hsize, c.hsize)
        self.assertEqual(vsize, c.vsize)
        self.assertEqual(field_of_view, pi/2)
        I = Matrix([
            [1,0,0,0],
            [0,1,0,0],
            [0,0,1,0],
            [0,0,0,1]
        ])
        self.assertTrue(matrix.equals(c.transform, I))

    def test_camera2(self):
        c = Camera(200, 125, pi/2)
        self.assertTrue(equals(c.pixel_size, 0.01))
    
    def test_camera3(self):
        c = Camera(125, 200, pi/2)
        self.assertTrue(equals(c.pixel_size, 0.01))

    def test_camera4(self):
        c = Camera(201, 101, pi/2)
        r = c.ray_for_pixel(100, 50)
        self.assertTrue(r.origin.equals(Point(0, 0, 0)))
        self.assertTrue(r.direction.equals(Vector(0, 0, -1)))
    
    def test_camera5(self):
        c = Camera(201, 101, pi/2)
        r = c.ray_for_pixel(0, 0)
        self.assertTrue(r.origin.equals(Point(0, 0, 0)))
        self.assertTrue(r.direction.equals(Vector(0.66519, 0.33259, -0.66851)))
    
    def test_camera6(self):
        c = Camera(201, 101, pi/2)
        c.transform = rotate_y(pi/4) * translate(0, -2, 5)
        r = c.ray_for_pixel(100, 50)
        self.assertTrue(r.origin.equals(Point(0, 2, -5)))
        self.assertTrue(r.direction.equals(Vector(sqrt(2)/2, 0, -sqrt(2)/2)))
    
    def test_camera7(self):
        w = World()
        c = Camera(11, 11, pi/2)
        pfrom = Point(0, 0, -5)
        pto = Point(0, 0, 0)
        vup = Vector(0, 1, 0)
        c.transform = view_transform(pfrom, pto, vup)
        image = c.render(w)
        self.assertTrue(Color(0.38066, 0.47583, 0.2855).equals(image.pixel_at(5, 5)))



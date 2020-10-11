from math import sqrt, pi
import unittest
from io import StringIO
from base import Base
from point import Point
from vector import Vector
import color
from color import Color
from misc import equals
from canvas import Canvas
import matrix
from matrix import Matrix
from transform import translate, scale, rotate_x, rotate_y, rotate_z, shear
from ray import Ray


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


class test_canvas(unittest.TestCase):
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
    
        


class test_matrix(unittest.TestCase):
    def test_create1(self):
        A =    Matrix([[1, 2, 3, 4],
                       [5, 6, 7, 8],
                       [9, 8, 7, 6],
                       [5, 4, 3, 2]])
        B =    Matrix([[1, 2, 3, 4],
                       [5, 6, 7, 8],
                       [9, 8, 7, 6],
                       [5, 4, 3, 2]])
        self.assertTrue(matrix.equals(A, B))
                
    def test_create2(self):
        A =    Matrix([[1, 2, 3, 4],
                       [5, 6, 7, 8],
                       [9, 8, 7, 6],
                       [5, 4, 3, 2]])
        B =    Matrix([[2, 2, 3, 4],
                       [5, 6, 7, 8],
                       [9, 8, 7, 6],
                       [5, 4, 3, 2]])
        self.assertFalse(matrix.equals(A, B))
    
    def test_mul1(self):
        A =    Matrix([[1, 2, 3, 4],
                       [5, 6, 7, 8],
                       [9, 8, 7, 6],
                       [5, 4, 3, 2]])
        B =    Matrix([[-2, 1, 2, 3],
                       [3, 2, 1, -1],
                       [4, 3, 6, 5],
                       [1, 2, 7, 8]])
        C =    Matrix([[20, 22, 50, 48],
                       [44, 54, 114, 108],
                       [40, 58, 110, 102],
                       [16, 26, 46, 42]])
        self.assertTrue(matrix.equals(C, A*B))
    
    def test_mul2(self):
        A =    Matrix([[1, 2, 3, 4],
                       [2, 4, 4, 2],
                       [8, 6, 4, 1],
                       [0, 0, 0, 1]])
        b = Base(1, 2, 3, 1)
        self.assertTrue(Base(18, 24, 33, 1).equals(A*b))
    
    def test_ide1(self):
        I = Matrix([[1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])
        A =    Matrix([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 8, 7, 6],
                    [5, 4, 3, 2]])
        self.assertTrue(matrix.equals(A,A*I))
    
    def test_tranpose1(self):
        A = Matrix([[0, 9, 3, 0],
                    [9, 8, 0, 8],
                    [1, 8, 5, 3],
                    [0, 0, 5, 8]])
        B = Matrix([[0, 9, 1, 0],
                    [9, 8, 8, 0],
                    [3, 0, 5, 5],
                    [0, 8, 3, 8]])
        self.assertTrue(matrix.equals(A.transpose(),B))
                    
    def test_det1(self):
        A = Matrix([[1, 5],
                    [-3, 2]])
        self.assertEqual(A.determinant(), 17)
    
    def test_subm1(self):
        A = Matrix([[1, 5, 0],
                    [-3, 2, 7],
                    [0, 6, -3]])
        B = Matrix([[-3, 2],
                    [0, 6]])
        self.assertTrue(matrix.equals(A.submatrix(0,2), B))
    
    def test_subm2(self):
        A = Matrix([[-6, 1, 1, 6],
                    [-8, 5, 8, 6],
                    [-1, 0, 8, 2],
                    [-7, 1, -1, 1]])
        B = Matrix([[-6, 1, 6],
                    [-8, 8, 6],
                    [-7, -1, 1]])
        self.assertTrue(matrix.equals(A.submatrix(2, 1), B))

    def test_subm3(self):
        A = Matrix([[3, 5, 0],
                    [2, -1, 7],
                    [6, -1, 5]])

        B = Matrix([[5, 0],
                    [-1, 5]])

        self.assertTrue(matrix.equals(A.submatrix(1, 0), B))

    def test_minor1(self):
        A = Matrix([[3, 5, 0],
                    [2, -1, 7],
                    [6, -1, 5]])

        B = A.submatrix(1, 0)

        C = Matrix([[5, 0],
                    [-1, 5]])

        self.assertTrue(matrix.equals(A.submatrix(1, 0), C))
        self.assertEqual(B.determinant(), 25)
        self.assertEqual(A.minor(1, 0), 25)
    
    def test_cofactor1(self):
        A = Matrix([[3, 5, 0],
                    [2, -1, -7],
                    [6, -1, 5]])
        self.assertEqual(A.minor(0, 0), -12)
        self.assertEqual(A.cofactor(0, 0), -12)
        self.assertEqual(A.minor(1, 0), 25)
        self.assertEqual(A.cofactor(1, 0), -25)
    
    def test_det2(self):
        A = Matrix([[1, 2, 6],
                    [-5, 8, -4],
                    [2, 6, 4]])
        self.assertEqual(A.cofactor(0, 0), 56)
        self.assertEqual(A.cofactor(0, 1), 12)
        self.assertEqual(A.cofactor(0, 2), -46)
        self.assertEqual(A.determinant(), -196)

    def test_det3(self):
        A = Matrix([[-2,  -8, 3, 5],
                    [-3,  1, 7, 3],
                    [1,  2, -9, 6],
                    [-6,  7, 7, -9]])
        self.assertEqual(A.cofactor(0, 0), 690)
        self.assertEqual(A.cofactor(0, 1), 447)
        self.assertEqual(A.cofactor(0, 2), 210)
        self.assertEqual(A.cofactor(0, 3), 51)
        self.assertEqual(A.determinant(), -4071)
    
    def test_inv1(self):
        A = Matrix([[6, 4, 4, 4],
                    [5, 5, 7, 6],
                    [4, -9, 3, -7],
                    [9, 1, 7, -6]]) 
        self.assertEqual(A.determinant(), -2120)
        self.assertTrue(A.is_invertible())

    def test_inv2(self):
        A = Matrix([[-4, 2, -2, -3,],
                    [9, 6, 2, 6],
                    [0, -5, 1, -5],
                    [0, 0, 0, 0]])
        self.assertEqual(A.determinant(), 0)
        self.assertFalse(A.is_invertible())

    def test_inv3(self):
        A = Matrix([[-5 , 2 , 6 , -8 ],
                    [1 , -5 , 1 , 8 ],
                    [7 , 7 , -6 , -7 ],
                    [1 , -3 , 7 , 4 ]])
        B = A.inverse()
        C = Matrix([[ 0.21805,  0.45113,  0.24060, -0.04511],
                    [-0.80827, -1.45677, -0.44361,  0.52068],
                    [-0.07895, -0.22368, -0.05263,  0.19737],
                    [-0.52256, -0.81391, -0.30075,  0.30639]])
        
        self.assertEqual(A.determinant(), 532)
        self.assertEqual(A.cofactor(2, 3), -160)
        self.assertEqual(B[3][2], -160./532)
        self.assertEqual(A.cofactor(3, 2), 105)
        self.assertEqual(B[2][3], 105./532)
        self.assertTrue(matrix.equals(B,C))
        
    def test_inv4(self):
        A = Matrix([[ 8, -5,  9,  2],
                    [ 7,  5,  6,  1],
                    [-6,  0,  9,  6],
                    [-3,  0, -9, -4]])
        B = Matrix([[-0.15385, -0.15385, -0.28205, -0.53846],
                    [-0.07692,  0.12308,  0.02564,  0.03077],
                    [ 0.35897,  0.35897,  0.43590,  0.92308],
                    [-0.69231, -0.69231, -0.76923, -1.92308]])
        self.assertTrue(matrix.equals(A.inverse(),B))

    def test_inv5(self):
        A = Matrix([[ 9,  3,  0,  9],
                    [-5, -2, -6, -3],
                    [-4,  9,  6,  4],
                    [-7,  6,  6,  2]])
        B = Matrix([[-0.04074, -0.07778,  0.14444, -0.22222],
                    [-0.07778,  0.03333,  0.36667, -0.33333],
                    [-0.02901, -0.14630, -0.10926,  0.12963],
                    [ 0.17778,  0.06667, -0.26667,  0.33333]])
        self.assertTrue(matrix.equals(A.inverse(),B))

    def test_inv6(self):
        A = Matrix([[ 3, -9,  7,  3],
                    [ 3, -8,  2, -9],
                    [-4,  4,  4,  1],
                    [-6,  5, -1,  1]])
        B = Matrix([[8,  2, 2, 2],
                    [3, -1, 7, 0],
                    [7,  0, 5, 4],
                    [6, -2, 0, 5]])
        C = A*B
        self.assertTrue(matrix.equals(C*B.inverse(),A))

class test_transform(unittest.TestCase):
    def test_transform1(self):
        t = translate(5, -3, 2)
        p = Point(-3, 4, 5)
        self.assertTrue(Point(2, 1, 7).equals(t*p))
    
    def test_transform2(self):
        t = translate(5, -3, 2)
        inv = t.inverse()
        p = Point(-3, 4, 5)
        self.assertTrue(Point(-8, 7, 3).equals(inv*p))
    
    def test_transform3(self):
        t = translate(5, -3, 2)
        v = Vector(-3, 4, 5)
        self.assertTrue(v.equals(t*v))
    
    def test_scale1(self):
        s = scale( 2, 3, 4)
        p = Point(-4, 6, 8)
        self.assertTrue(Point(-8, 18, 32).equals(s*p))

    def test_scale2(self):
        s = scale( 2, 3, 4)
        v = Vector(-4, 6, 8)
        self.assertTrue(Vector(-8, 18, 32).equals(s*v))

    def test_scale3(self):
        s = scale( 2, 3, 4)
        inv = s.inverse()
        v = Vector(-4, 6, 8)
        self.assertTrue(Vector(-2, 2, 2).equals(inv*v))

    def test_scale4(self):
        s = scale(-1, 1, 1)
        p = Point(2, 3, 4)
        self.assertTrue(Point(-2, 3, 4).equals(s*p))
    
    def test_rotate1(self):
        p = Point(0, 1, 0)
        half_quarter = rotate_x(pi/4)
        full_quarter = rotate_x(pi/2)
        self.assertTrue(Point(0, sqrt(2)/2, sqrt(2)/2).equals(half_quarter*p))
        self.assertTrue(Point(0, 0, 1).equals(full_quarter*p))



    def test_rotate2(self):
        p = Point(0, 1, 0)
        half_quarter = rotate_x(pi/4)
        inv = half_quarter.inverse()
        self.assertTrue(Point(0, sqrt(2)/2, -sqrt(2)/2).equals(inv*p))


    def test_rotate3(self):
        p = Point(0, 0, 1)
        half_quarter = rotate_y(pi/4)
        full_quarter = rotate_y(pi/2)
        self.assertTrue(Point(sqrt(2)/2, 0, sqrt(2)/2).equals(half_quarter*p))
        self.assertTrue(Point(1, 0, 0).equals(full_quarter*p))

    def test_rotate4(self):
        p = Point(0, 1, 0)
        half_quarter = rotate_z(pi/4)
        full_quarter = rotate_z(pi/2)
        self.assertTrue(Point(-sqrt(2)/2, sqrt(2)/2, 0).equals(half_quarter*p))
        self.assertTrue(Point(-1, 0, 0).equals(full_quarter*p))
    
    def test_shear1(self):
        p = Point(2, 3, 4)
        s = shear(1, 0, 0, 0, 0, 0)
        self.assertTrue(Point(5, 3, 4).equals(s*p))

    def test_shear2(self):
        p = Point(2, 3, 4)
        s = shear(0, 1, 0, 0, 0, 0)
        self.assertTrue(Point(6, 3, 4).equals(s*p))

    def test_shear3(self):
        p = Point(2, 3, 4)
        s = shear(0, 0, 1, 0, 0, 0)
        self.assertTrue(Point(2, 5, 4).equals(s*p))

    def test_shear4(self):
        p = Point(2, 3, 4)
        s = shear(0, 0, 0, 1, 0, 0)
        self.assertTrue(Point(2, 7, 4).equals(s*p))

    def test_shear5(self):
        p = Point(2, 3, 4)
        s = shear(0, 0, 0, 0, 1, 0)
        self.assertTrue(Point(2, 3, 6).equals(s*p))

    def test_shear6(self):
        p = Point(2, 3, 4)
        s = shear(0, 0, 0, 0, 0, 1)
        self.assertTrue(Point(2, 3, 7).equals(s*p))

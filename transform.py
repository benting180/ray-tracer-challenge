import matrix
from matrix import Matrix
from math import cos, sin

def translate(x, y, z):
    return  Matrix([[1, 0, 0, x],
                    [0, 1, 0, y],
                    [0, 0, 1, z],
                    [0, 0, 0, 1]])

def scale(x, y, z):
    return  Matrix([[x, 0, 0, 0],
                    [0, y, 0, 0],
                    [0, 0, z, 0],
                    [0, 0, 0, 1]])

def rotate_x(r):
    return  Matrix([[1, 0, 0, 0],
                    [0, cos(r), -sin(r), 0],
                    [0, sin(r), cos(r), 0],
                    [0, 0, 0, 1]])

def rotate_y(r):
    return  Matrix([[cos(r), 0, sin(r), 0],
                    [0, 1, 0, 0],
                    [-sin(r), 0, cos(r), 0],
                    [0, 0, 0, 1]])

def rotate_z(r):
    return  Matrix([[cos(r), -sin(r), 0, 0],
                    [sin(r), cos(r), 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])

def shear(xy, xz, yx, yz, zx, zy):
    return  Matrix([[1, xy, xz, 0],
                    [yx, 1, yz, 0],
                    [zx, zy, 1, 0],
                    [0, 0, 0, 1]])

def view_transform(pfrom, pto, vup):
    forward = (pto - pfrom).normalize()
    uvup = vup.normalize()
    left = forward.cross(uvup)
    true_up = left.cross(forward)

    orientation = Matrix([
        [left.x, left.y, left.z, 0],
        [true_up.x, true_up.y, true_up.z, 0],
        [-forward.x, -forward.y, -forward.z, 0],
        [0, 0, 0, 1]
    ])
    t = translate(-pfrom.x, -pfrom.y, -pfrom.z)
    return orientation * t
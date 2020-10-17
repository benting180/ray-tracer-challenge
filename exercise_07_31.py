from math import pi
from transform import rotate_x, scale, translate, scale, shear, rotate_z, rotate_y, view_transform
from vector import Vector
from matrix import Matrix
from canvas import Canvas
from point import Point
from color import Color
from ray import Ray
from sphere import Sphere
from material import Material
from light import Light
from time import time
from world import World
from camera import Camera


if __name__ == '__main__':
    t1 = time()


    floor = Sphere()
    floor.transform = scale(10, 0.01, 10)
    floor.material = Material()
    floor.material.color = Color(1, 0.9, 0.9)
    floor.material.specular = 0

    left_wall = Sphere()
    left_wall.transform = translate(0, 0, 5) * \
        rotate_y(-pi/4) * \
        rotate_x(pi/2) * \
        scale(10, 0.01, 10)
    left_wall.material = floor.material

    right_wall = Sphere()
    right_wall.transform = translate(0, 0, 5) * \
        rotate_y(pi/4) * \
        rotate_x(pi/2) * \
        scale(10, 0.01, 10)
    right_wall.material = floor.material

    left = Sphere()
    left.transform = translate(-1.5, 0.33, -0.75) * \
        scale(0.33, 0.33, 0.33)
    left.material = Material()
    left.material.color = Color(0.9, 0.1, 0.1)
    left.material.diffuse = 0.7
    left.material.specular = 0.3
    
    middle = Sphere()
    middle.transform = translate(-0.5, 1, 0.5)
    middle.material = Material()
    middle.material.color = Color(0.1, 0.9, 0.1)
    middle.material.diffuse = 0.7
    middle.material.specular = 0.3

    right = Sphere()
    right.transform = translate(1.5, 0.5, -0.5) * \
        scale(0.5, 0.5, 0.5)
    right.material = Material()
    right.material.color = Color(0.1, 0.1, 0.9)
    right.material.diffuse = 0.7
    right.material.specular = 0.3

    objs = [
        floor,
        left_wall,
        right_wall,
        # middle,
        # right,
        # left
    ]

    
    for i in range(10):
        ball = Sphere()
        ball.transform = translate(0, 1, 1.) * rotate_z(pi*2/10*i) * translate(1, 0, 0) * scale(0.2, 0.2, 0.2)
        ball.material.color = Color(i*0.1, 1-i*0.1, 1-i*0.1)
        objs.append(ball)


    world = World()
    world.light = Light(Point(-10, 10, -10), Color(1, 1, 1))
    world.objs = objs

    camera = Camera(100, 50, pi/3)
    camera.transform = view_transform(
        Point(0, 1.5, -5),
        Point(0, 1, 0),
        Vector(0, 1, 0)
    )

    canvas = camera.render(world)

    with open('test_034.ppm', 'w') as fout:
        canvas.to_ppm(fout)

    t2 = time()
    print("Time spent: {:.2f}s".format(t2-t1))

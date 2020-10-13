from math import pi
from transform import rotate_x, scale, translate, scale, shear, rotate_z

from matrix import Matrix
from canvas import Canvas
from point import Point
from color import Color
from ray import Ray
from sphere import Sphere
from material import Material
from light import Light
from time import time


if __name__ == '__main__':
    t1 = time()
    pixel_size = 100
    WIDTH = 100
    HEIGHT = 100
    c = Canvas(WIDTH, HEIGHT, Color(0.5, 0.5, 0.5))
    sphere = Sphere(Point(0, 0, 0), radius=1)
    m = Material()
    m.color = Color(1, 0.2, 1)
    sphere.material = m
    light = Light(Point(-10, 10, -10), Color(1, 1, 1))

    # sphere.set_transform(rotate_z(pi/6)* scale(1, 0.5, 1)*shear(1, 0, 0, 0, 0, 0))
    camera = Point(0, 0, -5)
    wall_z = 10
    wall_size = 7
    canvas_pixels = 100
    pixel_size = wall_size / canvas_pixels
    half = wall_size / 2
    for j in range(HEIGHT):
        print(j)
        y = half - pixel_size * j
        for i in range(WIDTH):
            x = -half + pixel_size*i
            target = Point(x, y, wall_z)
            
            ray = Ray(camera, (target-camera).normalize())
            intersections = sphere.intersect(ray)
            intersection = intersections.hit()
            if intersection is not None:
                point = ray.position(intersection.t)
                normal = intersection.obj.normal_at(point)
                eye = -ray.direction
                color = intersection.obj.material.lighting(light, point, eye, normal)
                c.write_pixel(i, j, color)
            # print(j, "target: ", target, obj.t)

    with open('test_016.ppm', 'w') as fout:
        c.to_ppm(fout)
    
    t2 = time()
    print("Time spent: {:.2f}s".format(t2-t1))

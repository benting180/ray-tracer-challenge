from math import pi
from transform import rotate_x, scale, translate, scale, shear, rotate_z

from matrix import Matrix
from canvas import Canvas
from point import Point
from color import Color
from ray import Ray
from sphere import Sphere

if __name__ == '__main__':
    pixel_size = 100
    WIDTH = 100
    HEIGHT = 100
    c = Canvas(WIDTH, HEIGHT, Color(0.5, 0.5, 0.5))
    sphere = Sphere(Point(0, 0, 0), radius=1)
    sphere.set_transform(rotate_z(pi/6)* scale(1, 0.5, 1)*shear(1, 0, 0, 0, 0, 0))
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
            obj = intersections.hit()
            if obj is not None:
                c.write_pixel(i, j, Color(255, 0, 0))
            # print(j, "target: ", target, obj.t)

    with open('test_013.ppm', 'w') as fout:
        c.to_ppm(fout)

    # while True:

    # orig = Point(0., 1., 0.)
    # p = orig
    # run = True
    # for i in range(12):
    #     p = rotate(p)
    #     print(p)


    #     i = WIDTH//2 + round(p.y*200)
    #     j = HEIGHT//2 + round(p.z*200)

    #     print(i, j)
    #     for di in [-2, -1, 0, 1, 2]:
    #         for dj in [-2, -1, 0, 1, 2]:
    #             if i+di < WIDTH and i+di >= 0 and j+dj < HEIGHT and j+dj >= 0:
    #                 c.write_pixel(i+di, j+dj, Color(255, 0, 0))
    #             else:
    #                 run = False
                
    # with open('test_007.ppm', 'w') as fout:
    #     c.to_ppm(fout)
from math import pi
from transform import rotate_x, scale, translate

from matrix import Matrix
from canvas import Canvas
from point import Point
from color import Color

def rotate(p):
    return rotate_x(pi/6) * p



if __name__ == '__main__':
    WIDTH = 600
    HEIGHT = 600
    c = Canvas(WIDTH, HEIGHT, Color(0.5, 0.5, 0.5))
    # while True:

    orig = Point(0., 1., 0.)
    p = orig
    run = True
    for i in range(12):
        p = rotate(p)
        print(p)


        i = WIDTH//2 + round(p.y*200)
        j = HEIGHT//2 + round(p.z*200)

        print(i, j)
        for di in [-2, -1, 0, 1, 2]:
            for dj in [-2, -1, 0, 1, 2]:
                if i+di < WIDTH and i+di >= 0 and j+dj < HEIGHT and j+dj >= 0:
                    c.write_pixel(i+di, j+dj, Color(255, 0, 0))
                else:
                    run = False
                
    with open('test_007.ppm', 'w') as fout:
        c.to_ppm(fout)
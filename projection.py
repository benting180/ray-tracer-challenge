from color import Color
from vector import Vector
from point import Point
from canvas import Canvas
from projectile import Projectile
from environment import Environment


def tick(env, proj):
    position = proj.position + proj.velocity
    velocity = proj.velocity + env.gravity + env.wind
    return Projectile(position, velocity)

if __name__ == '__main__':
    p = Projectile(Point(0, 1, 0), Vector(1.5, 1.0, 0))
    e = Environment(Vector(0, -0.1, 0), Vector(-0.01, 0, 0))
    WIDTH = 900
    HEIGHT = 550
    c = Canvas(WIDTH, HEIGHT)
    # while True:
    run = True
    while run:
        p = tick(e, p)
        i = round(p.position.x*10)
        j = 550 - round(p.position.y*10)

        print(i, j)
        for di in [-2, -1, 0, 1, 2]:
            for dj in [-2, -1, 0, 1, 2]:
                if i+di < WIDTH and i+di >= 0 and j+dj < HEIGHT and j+dj >= 0:
                    c.write_pixel(i+di, j+dj, Color(255, 0, 0))
                    # print('write')
                else:
                    run = False
                
    with open('test_006.ppm', 'w') as fout:
        c.to_ppm(fout)

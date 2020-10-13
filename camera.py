from point import Point
from math import tan
from ray import Ray
from matrix import Matrix
from canvas import Canvas


class Camera:
    def __init__(self, hsize, vsize, field_of_view):
        self.hsize = hsize
        self.vsize = vsize
        self.field_of_view = field_of_view
        I = Matrix([
            [1,0,0,0],
            [0,1,0,0],
            [0,0,1,0],
            [0,0,0,1]
        ])
        self.transform = I
        half_view = tan(field_of_view / 2)
        aspect = hsize / vsize

        if aspect >= 1:
            half_width = half_view
            half_height = half_width / aspect
        else:
            half_height = half_view
            half_width = half_height * aspect
        self.half_width = half_width
        self.half_height = half_height
        self.pixel_size = half_width * 2 / hsize
    
    def ray_for_pixel(self, px, py):
        xoffset = (px + 0.5) * self.pixel_size
        yoffset = (py + 0.5) * self.pixel_size

        world_x = self.half_width - xoffset
        world_y = self.half_height - yoffset

        pixel = self.transform.inverse() * Point(world_x, world_y, -1)
        origin = self.transform.inverse() * Point(0, 0, 0)
        direction = (pixel - origin).normalize()
        return Ray(origin, direction)
    
    def render(self, world):
        image = Canvas(self.hsize, self.vsize)
        for j in range(self.vsize-1):
            for i in range(self.vsize-1):
                ray = self.ray_for_pixel(i, j)
                color = world.color_at(ray)
                image.write_pixel(i, j, color)

        return image

        
            
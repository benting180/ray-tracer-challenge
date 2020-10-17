from point import Point
from math import sqrt
from matrix import Matrix
from ray import Ray
from material import Material
from vector import Vector


class Shape:
    def __init__(self):
        self.transform = Matrix([[1, 0, 0, 0],
                               [0, 1, 0, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]])
        self.material = Material()

    def intersect(self, ray):
        local_ray = Ray(self.transform.inverse()*ray.origin, self.transform.inverse()*ray.direction)
        return self.local_intersect(local_ray)

    def set_transform(self, t):
        self.transform = t
    
    def normal_at(self, world_point):
        local_point = self.transform.inverse() * world_point
        local_normal = self.local_normal_at(local_point)
        world_normal = self.transform.inverse().transpose() * local_normal
        world_normal.w = 0
        return world_normal.normalize()

class TestShape(Shape):
    def __init__(self):
        Shape.__init__(self)
    
    def local_intersect(self, ray):
        self.saved_ray = ray
    
    def local_normal_at(self, point):
        return Vector(point.x, point.y, point.z)

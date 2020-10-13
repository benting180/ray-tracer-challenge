from point import Point
from math import sqrt
from matrix import Matrix
from intersections import Intersection, Intersections
from ray import Ray
from material import Material


class Sphere:
    def __init__(self, origin=Point(0, 0, 0), radius=1):
        self.origin = origin
        self.radius = radius
        self.transform = Matrix([[1, 0, 0, 0],
                               [0, 1, 0, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]])
        self.material = Material()

    def intersect(self, ray):
        # ray2 = self.transform.inverse() * ray
        ray = Ray(self.transform.inverse()*ray.origin, self.transform.inverse()*ray.direction)
        sphere2ray = ray.origin - Point(0, 0, 0)
        a = ray.direction.dot(ray.direction)
        b = 2 * ray.direction.dot(sphere2ray)
        c = sphere2ray.dot(sphere2ray) - 1
        discriminant = b*b - 4*a*c
        if discriminant < 0:
            return Intersections([])
        else:
            t1 = (- b - sqrt(discriminant))/(2*a)
            t2 = (- b + sqrt(discriminant))/(2*a)
            i1 = Intersection(t1, self)
            i2 = Intersection(t2, self)
            return Intersections([i1, i2])
    
    def __eq__(self, s):
        if isinstance(s, Sphere):
            return (self.origin == s.origin and
                    self.radius == s.radius)

    def set_transform(self, t):
        self.transform = t
    
    def normal_at(self, world_point):
        obj_point = self.transform.inverse() * world_point
        obj_normal = obj_point - Point(0, 0, 0)
        world_normal = self.transform.inverse().transpose() * obj_normal
        # print(world_normal.w)
        world_normal.w = 0
        return world_normal.normalize()

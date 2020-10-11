from point import Point
from math import sqrt
from intersections import Intersection, Intersections

class Sphere:
    def __init__(self, origin=Point(0, 0, 0), radius=1):
        self.origin = origin
        self.radius = radius

    def interset(self, ray):
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
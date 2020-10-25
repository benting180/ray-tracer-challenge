from point import Point
from math import sqrt
from matrix import Matrix
from intersections import Intersection, Intersections
from ray import Ray
from material import Material
from shape import Shape

class Sphere(Shape):
    def __init__(self, origin=Point(0, 0, 0), radius=1):
        Shape.__init__(self)
        self.origin = origin
        self.radius = radius
        self.parent = Shape

    def local_intersect(self, ray):
        # ray2 = self.transform.inverse() * ray
        # ray = Ray(self.transform.inverse()*ray.origin, self.transform.inverse()*ray.direction)
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
            return (
                self.origin == s.origin and
                self.radius == s.radius and
                self.material == s.material
            )
        else:
            return False
    
    def local_normal_at(self, local_point):
        local_normal = local_point - Point(0, 0, 0)
        return local_normal

class GlassSphere(Sphere):
    def __init__(self):
        Sphere.__init__(self)
        self.material.transparency = 1.0
        self.material.refractive_index = 1.5

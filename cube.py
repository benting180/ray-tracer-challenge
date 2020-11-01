from point import Point
from math import sqrt
from matrix import Matrix
from intersections import Intersection, Intersections
from ray import Ray
from material import Material
from shape import Shape
from misc import EPSILON
from vector import Vector

class Cube(Shape):
    def __init__(self, origin=Point(0, 0, 0), radius=1):
        Shape.__init__(self)
        self.origin = origin
        self.radius = radius
        self.parent = Shape

    def local_intersect(self, ray):
        xtmin, xtmax = self.check_axis(ray.origin.x, ray.direction.x)
        ytmin, ytmax = self.check_axis(ray.origin.y, ray.direction.y)
        ztmin, ztmax = self.check_axis(ray.origin.z, ray.direction.z)
        tmin = max(xtmin, ytmin, ztmin)
        tmax = min(xtmax, ytmax, ztmax)
        if tmin > tmax:
            return Intersections([])
        ls = [
            Intersection(tmin, self),
            Intersection(tmax, self)
        ]
        xs = Intersections(ls)
        return xs
    
    def check_axis(self, origin, direction):
        tmin_numerator = -1 - origin
        tmax_numerator = 1 - origin

        if abs(direction) >= EPSILON:
            tmin = tmin_numerator / direction
            tmax = tmax_numerator / direction
        else:
            tmin = tmin_numerator * float('inf')
            tmax = tmax_numerator * float('inf')
        
        if tmin > tmax:
            temp = tmin
            tmin = tmax
            tmax = temp
        return tmin, tmax
    
    def local_normal_at(self, point):
        maxc = max(abs(point.x), abs(point.y), abs(point.z))

        if maxc == abs(point.x):
            return Vector(point.x, 0, 0)
        elif maxc == abs(point.y):
            return Vector(0, point.y, 0)
        else:
            return Vector(0, 0, point.z)
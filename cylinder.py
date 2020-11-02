from point import Point
from math import sqrt
from matrix import Matrix
from intersections import Intersection, Intersections
from ray import Ray
from material import Material
from shape import Shape
from misc import EPSILON
from vector import Vector

class Cylinder(Shape):
    def __init__(self, minimum=float('-inf'), maximum=float('inf')):
        Shape.__init__(self)
        self.minimum = minimum
        self.maximum = maximum


    def local_intersect(self, ray):
        a = ray.direction.x**2 + ray.direction.z**2
        if a < EPSILON:
            return Intersections([])

        b = 2 * ray.origin.x * ray.direction.x + \
            2 * ray.origin.z * ray.direction.z
        c = ray.origin.x**2 + ray.origin.z**2 - 1
        disc = b**2 - 4 * a * c
        if disc < 0:
            return Intersections([])
        
        t0 = ( - b - sqrt(disc)) / (2 * a)
        t1 = ( - b + sqrt(disc)) / (2 * a)

        if t0 > t1:
            temp = t0
            t0 = t1
            t1 = temp

        ls = []

        y0 = ray.origin.y + t0 * ray.direction.y
        if self.minimum < y0 and y0 < self.maximum:
            ls.append(Intersection(t0, self))
        
        y0 = ray.origin.y + t1 * ray.direction.y
        if self.minimum < y0 and y0 < self.maximum:
            ls.append(Intersection(t1, self))

        return Intersections(ls)

    def local_normal_at(self, point):
        return Vector(point.x, 0, point.z)
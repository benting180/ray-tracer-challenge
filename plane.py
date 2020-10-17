from point import Point
from vector import Vector
from math import sqrt
from matrix import Matrix
from intersections import Intersection, Intersections
from ray import Ray
from material import Material
from shape import Shape
from misc import EPSILON

class Plane(Shape):
    def __init__(self, y = 0):
        Shape.__init__(self)
        self.y = y
        self.parent = Shape

    def local_intersect(self, ray):
        if abs(ray.direction.y) < EPSILON:
            return Intersections([])
        else:
            t1 = -ray.origin.y / ray.direction.y
            i1 = Intersection(t1, self)
            return Intersections([i1])
    
    def __eq__(self, s):
        if isinstance(s, Plane):
            return (
                self.y == s.y
            )
    
    def local_normal_at(self, local_point):
        return Vector(0, 1, 0)
        

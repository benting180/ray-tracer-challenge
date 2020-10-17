from math import floor, sqrt, pi
from matrix import Matrix
from color import Color
from transform import rotate_y, scale
from sphere import Sphere

class Pattern:
    def __init__(self):
        self.transform = Matrix([[1, 0, 0, 0],
                               [0, 1, 0, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]])

    def set_pattern_transform(self, transform):
        self.transform = transform
    
    def pattern_at_shape(self, obj, world_point):
        object_point = obj.transform.inverse() * world_point
        pattern_point = self.transform.inverse() * object_point
        return self.pattern_at(pattern_point)


class StripePattern(Pattern):
    def __init__(self, a, b):
        Pattern.__init__(self)
        self.a = a
        self.b = b
        
    def pattern_at(self, point):
        if floor(point.x) % 2 == 0:
            return self.a
        else:
            return self.b


class TestPattern(Pattern):
    def __init__(self):
        Pattern.__init__(self)

    def pattern_at(self, point):
        return Color(point.x, point.y, point.z)
    
class GradientPattern(Pattern):
    def __init__(self, a, b):
        Pattern.__init__(self)
        self.a = a
        self.b = b

    def pattern_at(self, point):
        distance = self.b - self.a
        fraction = point.x - floor(point.x)
        return self.a + distance * fraction

class RadialGradientPattern(Pattern):
    def __init__(self, a, b):
        Pattern.__init__(self)
        self.a = a
        self.b = b

    def pattern_at(self, point):
        distance = self.b - self.a
        r = point.magnitude()
        fraction = r - floor(r)
        return self.a + distance * fraction

class RingPattern(Pattern):
    def __init__(self, a, b):
        Pattern.__init__(self)
        self.a = a
        self.b = b

    def pattern_at(self, point):
        if floor(sqrt(point.x * point.x + point.z * point.z)) % 2 == 0:
            return self.a
        else:
            return self.b

class CheckerPattern(Pattern):
    def __init__(self, a, b):
        Pattern.__init__(self)
        self.a = a
        self.b = b

    def pattern_at(self, point):
        if (floor(point.x) + floor(point.y) + floor(point.z)) % 2 == 0:
            return self.a
        else:
            return self.b

class NestedPattern(Pattern):
    def __init__(self, p1=None, p2=None):
        Pattern.__init__(self)
        if p1 is None:
            p1 = StripePattern(Color(0.9, 0, 0), Color(0.9, 0.3, 0.0))
            p1.transform = scale(0.2, 0.2, 0.2) * rotate_y(pi/4)
        if p2 is None:
            p2 = StripePattern(Color(0.0, 0.0, 0.9), Color(0.0, 0.3, 0.9))
            p2.transform = scale(0.2, 0.2, 0.2) * rotate_y(-pi/4)
        self.p1 = p1
        self.p2 = p2

    def pattern_at(self, point):
        # return self.p1.pattern_at_shape(Sphere(), point)
        if (floor(point.x) + floor(point.z)) % 2 == 0:
            return self.p1.pattern_at_shape(Sphere(), point)
        else:
            return self.p2.pattern_at_shape(Sphere(), point)

class BlendedPattern(Pattern):
    def __init__(self, p1=None, p2=None):
        Pattern.__init__(self)
        if p1 is None:
            p1 = StripePattern(Color(0.9, 0, 0), Color(0.8, 0.8, 0.8))
            p1.transform = rotate_y(pi/4)
        if p2 is None:
            p2 = StripePattern(Color(0.0, 0.0, 0.9), Color(0.8, 0.8, 0.8))
            p2.transform = rotate_y(-pi/4)
        self.p1 = p1
        self.p2 = p2

    def pattern_at(self, point):
        c1 = self.p1.pattern_at_shape(Sphere(), point)
        c2 = self.p2.pattern_at_shape(Sphere(), point)
        return (c1+c2)/2.
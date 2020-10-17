from math import floor
from matrix import Matrix
from color import Color

class Pattern:
    def __init__(self):
        self.transform = Matrix([[1, 0, 0, 0],
                               [0, 1, 0, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]])

    def set_pattern_transform(self, transform):
        self.transform = transform
    
    def stripe_at_object(self, obj, world_point):
        object_point = obj.transform.inverse() * world_point
        pattern_point = self.transform.inverse() * object_point
        return self.stripe_at(pattern_point)


class StripePattern(Pattern):
    def __init__(self, a, b):
        Pattern.__init__(self)
        self.a = a
        self.b = b
        
    def stripe_at(self, point):
        if floor(point.x) % 2 == 0:
            return self.a
        else:
            return self.b


class TestPattern(Pattern):
    def __init__(self):
        Pattern.__init__(self)

    def stripe_at(self, point):
        return Color(point.x, point.y, point.z)
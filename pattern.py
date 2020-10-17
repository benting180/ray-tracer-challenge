from math import floor
from matrix import Matrix

class StripePattern:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.transform = Matrix([[1, 0, 0, 0],
                               [0, 1, 0, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]])

    def stripe_at(self, point):
        if floor(point.x) % 2 == 0:
            return self.a
        else:
            return self.b
    
    def set_pattern_transform(self, transform):
        self.transform = transform
    
    def stripe_at_object(self, obj, world_point):
        object_point = obj.transform.inverse() * world_point
        pattern_point = self.transform.inverse() * object_point
        return self.stripe_at(pattern_point)

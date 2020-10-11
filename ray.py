from point import Point


class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction
    
    def position(self, n):
        return self.origin + self.direction * n
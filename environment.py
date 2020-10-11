from point import Point
from vector import Vector


class Environment:
    def __init__(self, position, velocity):
        self.gravity = position
        self.wind = velocity
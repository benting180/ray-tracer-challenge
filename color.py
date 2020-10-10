from base import Base


class Color(Base):
    def __init__(self, r, g, b):
        self.x = r
        self.y = g
        self.z = b
        self.w = 0

def hadamard_product(c1, c2):
    return Color(c1.x*c2.x, c1.y*c2.y, c1.z*c2.z)
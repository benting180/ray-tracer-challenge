from math import sqrt
from base import Base


class Vector(Base):
    def __init__(self, x, y, z):
        super(self.__class__, self).__init__(x, y, z, 0)

    def mag(self):
        return sqrt(self.x*self.x + self.y*self.y + self.z*self.z + self.w*self.w)
    
    def normal(self):
        mag = self.mag()
        return Vector(self.x/mag, self.y/mag, self.z/mag)
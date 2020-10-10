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
    
    def dot(self, v):
        return self.x*v.x + self.y*v.y + self.z*v.z + self.w*v.w
    
    def cross(self, v):
        return Vector(self.y*v.z-self.z*v.y, self.z*v.x-self.x*v.z, self.x*v.y-self.y*v.x)
from misc import equals


class Base:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
    
    def __str__(self):
        return "Point: ({}, {}, {}, {})".format(self.x, self.y, self.z, self.w)

    def __add__(self, v):
        return Base(self.x+v.x, self.y+v.y, self.z+v.z, self.w+v.w)

    def __sub__(self, v):
        return Base(self.x-v.x, self.y-v.y, self.z-v.z, self.w-v.w)
    
    def __neg__(self):
        return Base(-self.x, -self.y, -self.z, -self.w)
    
    def __mul__(self, a):
        return Base(self.x*a, self.y*a, self.z*a, self.w*a)
        
    def __truediv__(self, a):
        return  self.__mul__(1./a)

    
    def equals(self, v):
        return equals(self.x, v.x) and \
                equals(self.y, v.y) and \
                equals(self.z, v.z) and \
                equals(self.w, v.w)


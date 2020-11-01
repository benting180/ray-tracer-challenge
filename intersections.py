from misc import EPSILON
from math import sqrt

class Comps:
    def __init__(self, t, obj, point, eyev, normalv, inside, over_point, under_point, reflectv, n1=1.0, n2=1.0):
        self.t = t
        self.obj = obj
        self.point = point
        self.eyev = eyev
        self.normalv = normalv
        self.inside = inside
        self.over_point = over_point
        self.under_point = under_point
        self.reflectv = reflectv
        self.n1 = n1
        self.n2 = n2
    
    def schlick(self):
        cos = self.eyev.dot(self.normalv)
        if self.n1 > self.n2:
            n = self.n1 / self.n2
            sin2_t = n*n * (1.0 - cos**2)
            if sin2_t > 1.0:
                return 1.0
            
            cos_t = sqrt(1.0 - sin2_t)
            cos = cos_t
        r0 = ((self.n1 - self.n2) / (self.n1 + self.n2))**2
        return r0 + (1 - r0) * (1 - cos) ** 5


class Intersections:
    def __init__(self, ls):
        self.count = len(ls)
        self.ls = ls
    
    def __getitem__(self, key):
        return self.ls[key]
    
    def __eq__(self, xs):
        if not isinstance(xs, Intersections):
            raise TypeError
        if self.count != xs.count:
            return False
        for i, x in enumerate(self.ls):
            if not (x == xs[i]):
                return False
        return True
    
    def hit(self):
        result = None
        for x in self.ls:
            if x.t >= 0:
                if result is None:
                    result = x
                elif x.t < result.t:
                    result = x
        return result


class Intersection:
    def __init__(self, t, obj):
        self.t = t
        self.obj = obj
    
    def __eq__(self, i):
        return (
            isinstance(i, Intersection) and
            self.t == i.t and
            self.obj == i.obj
        )


    
    def prepare_computations(self, ray, xs=Intersections(ls=[])):
        t = self.t
        obj = self.obj
        point = ray.position(t)
        eyev = -ray.direction
        normalv = obj.normal_at(point)
        
        # print(t, normalv, eyev, normalv.dot(eyev))
        if normalv.dot(eyev) < 0:
            inside = True
            normalv = -normalv
        else:
            inside = False
        reflectv = ray.direction.reflect(normalv)

        over_point = point + normalv * EPSILON
        under_point = point - normalv * EPSILON

        containers = []
        comps = Comps(t, obj, point, eyev, normalv, inside, over_point, under_point, reflectv)
        for j, i in enumerate(xs.ls):
            if i == self:
                if len(containers) == 0:
                    comps.n1 = 1.0
                else:
                    comps.n1 = containers[-1].material.refractive_index

            found = False
            for element in containers:
                if i.obj == element:
                    containers.remove(element)
                    found = True
                    # break
            if not found:
                containers.append(i.obj)
            
            if i == self:
                if len(containers) == 0:
                    comps.n2 = 1.0
                else:
                    comps.n2 = containers[-1].material.refractive_index
                break
            
        return comps


    

class Comps:
    def __init__(self, t, obj, point, eyev, normalv, inside):
        self.t = t
        self.obj = obj
        self.point = point
        self.eyev = eyev
        self.normalv = normalv
        self.inside = inside

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
    
    def prepare_computations(self, ray):
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
        comps = Comps(t, obj, point, eyev, normalv, inside)
        return comps

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
            if x.t > 0:
                if result is None:
                    result = x
                elif x.t < result.t:
                    result = x
        return result

    

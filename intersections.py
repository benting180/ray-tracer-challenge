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

    

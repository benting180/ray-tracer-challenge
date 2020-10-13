from light import Light
from sphere import Sphere
from point import Point
from color import Color
from material import Material
from transform import scale
from intersections import Intersections

class World:
    def __init__(self, light=Light(Point(-10, 10, -10), Color(1, 1, 1))):
        self.light = light
        m1 = Material(Color(0.8, 1.0, 0.6), 0.1, 0.7, 0.2)
        s1 = Sphere()
        s1.material = m1

        s2 = Sphere()
        t2 = scale(0.5, 0.5, 0.5)
        s2.set_transform(t2)
        self.objs = [s1, s2]

    def intersect(self, ray):
        def swap(l, i1, i2):
            temp = l[i1]
            l[i1] = l[i2]
            l[i2] = temp
            return l

        ls = []
        for obj in self.objs:
            interestion = obj.intersect(ray)
            if interestion.count != 0:
                ls.append(interestion[0])
                ls.append(interestion[1])
        
        n = len(ls)
        for i in range(1, n):
            target = ls[i].t
            for j in range(i):
                if ls[j].t > ls[i].t:
                    l = swap(ls, i, j)
        
        return Intersections(ls)

    def shade_hit(self, comps):
        m = comps.obj.material
        return m.lighting(self.light, comps.point, comps.eyev, comps.normalv)
    
    def color_at(self, ray):
        intersections = self.intersect(ray)
        intersection = intersections.hit()
        if intersection is None:
            color = Color(0, 0, 0)
        else:
            comps = intersection.prepare_computations(ray)
            color = self.shade_hit(comps)
        return color
        # if intersections.count == 0:
        #     color = Color(0, 0, 0)
        # else:
        #     comps = intersections[0].prepare_computations(ray)
        #     color = self.shade_hit(comps)
        # return color



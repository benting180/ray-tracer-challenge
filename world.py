from light import Light
from sphere import Sphere
from point import Point
from color import Color
from material import Material
from transform import scale
from intersections import Intersections
from ray import Ray
from math import sqrt

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
            intersections = obj.intersect(ray)
            if intersections.count != 0:
                for i in range(intersections.count):
                    ls.append(intersections[i])
        
        n = len(ls)
        for i in range(1, n):
            target = ls[i].t
            for j in range(i):
                if ls[j].t > ls[i].t:
                    l = swap(ls, i, j)
        
        return Intersections(ls)

    def shade_hit(self, comps, remaining=2):
        if remaining == 0:
            return Color(0, 0, 0)
        m = comps.obj.material
        is_shadowed = self.is_shadowed(comps.over_point)
        surface = m.lighting(comps.obj, self.light, comps.over_point, comps.eyev, comps.normalv, is_shadowed)
        reflected = self.reflected_color(comps, remaining)
        return surface + reflected
    
    def color_at(self, ray, remaining=2):
        if remaining == 0:
            return Color(0, 0, 0)
        intersections = self.intersect(ray)
        intersection = intersections.hit()
        if intersection is None:
            color = Color(0, 0, 0)
        else:
            comps = intersection.prepare_computations(ray)
            color = self.shade_hit(comps, remaining)
        return color
        # if intersections.count == 0:
        #     color = Color(0, 0, 0)
        # else:
        #     comps = intersections[0].prepare_computations(ray)
        #     color = self.shade_hit(comps)
        # return color
    
    def is_shadowed(self, point):
        v = (self.light.position - point)
        distance = v.magnitude()
        direction = v.normalize()

        r = Ray(point, direction)
        intersections = self.intersect(r)
        h = intersections.hit()
        if h is not None and h.t < distance:
            return True
        else:
            return False
    
    def reflected_color(self, comps, remaining=4):
        if remaining <= 0:
            return Color(0, 0, 0)
        if comps.obj.material.reflective == 0:
            return Color(0, 0, 0)
        reflect_ray = Ray(comps.over_point, comps.reflectv)
        color = self.color_at(reflect_ray, remaining - 1)
        return comps.obj.material.reflective * color

    def refracted_color(self, comps, remaining):
        if remaining == 0:
            return Color(0, 0, 0)
        if comps.obj.material.transparency == 0:
            return Color(0, 0, 0)

        n_ratio = comps.n1 / comps.n2
        cos_i = comps.eyev.dot(comps.normalv)

        # sin_i = sqrt(1-cos_i*cos_i)
        # sin_t = n_ratio * sin_i
        # if sin_t > 1:
        #     return Color(0, 0, 0)
        # cos_t = sqrt(1-sin_t*sin_t)

        sin2_t = n_ratio**2 * (1-cos_i**2)
        if sin2_t > 1:
            return Color(0, 0, 0)
        cos_t = sqrt(1.0 - sin2_t)

        direction = comps.normalv * (n_ratio * cos_i - cos_t) - \
                    comps.eyev * n_ratio

        refract_ray = Ray(comps.under_point, direction)
        # print(refract_ray.direction)

        color = self.color_at(refract_ray, remaining-1) * comps.obj.material.transparency
        
        return color

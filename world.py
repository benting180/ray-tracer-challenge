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
        s1 = Sphere()
        s1.material.color = Color(0.8, 1.0, 0.6)
        s1.material.diffuse = 0.7
        s1.material.specular = 0.2

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
    def shade_hit(self, comps, remaining=4):
        if remaining == 0:
            return Color(0, 0, 0)
        m = comps.obj.material
        is_shadowed = self.is_shadowed(comps.over_point)
        surface = m.lighting(comps.obj,
                            self.light,
                            comps.over_point,
                            comps.eyev,
                            comps.normalv,
                            is_shadowed)

        reflected = self.reflected_color(comps, remaining)
        refracted = self.refracted_color(comps, remaining)
        # print("refracted ", refracted)

        material = comps.obj.material
        if material.reflective > 0 and material.transparency > 0:
            reflectance = comps.schlick()
            return surface + reflected * reflectance + \
                            refracted * (1 - reflectance)
        return surface + reflected + refracted

    def color_at(self, ray, remaining=4):
        if remaining == 0:
            return Color(0, 0, 0)
        intersections = self.intersect(ray)
        intersection = intersections.hit()
        if intersection is None:
            color = Color(0, 0, 0)
        else:
            comps = intersection.prepare_computations(ray, intersections)
            color = self.shade_hit(comps, remaining)
        return color
    
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
        if remaining <= 0 or comps.obj.material.reflective == 0:
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

        sin2_t = n_ratio*n_ratio * (1-cos_i*cos_i)
        if sin2_t > 1:
            return Color(0, 0, 0)

        cos_t = sqrt(1.0 - sin2_t)
        direction = comps.normalv * (n_ratio * cos_i - cos_t) - \
                    comps.eyev * n_ratio

        refract_ray = Ray(comps.under_point, direction)

        temp1 = self.color_at(refract_ray, remaining-1)
        temp2 = comps.obj.material.transparency
        color = temp1 * temp2
        
        return color
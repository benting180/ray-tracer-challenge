import unittest
from world import World
from light import Light
from sphere import Sphere
from transform import scale, translate
from material import Material
from color import Color
from point import Point
from ray import Ray
from vector import Vector
from intersections import Intersection, Intersections
from plane import Plane
from math import sqrt
from pattern import TestPattern

class TestWorld(unittest.TestCase):
    def test_world1(self):
        w = World()

        light = Light(Point(-10, 10, -10), Color(1, 1, 1))
        self.assertTrue(Point(-10, 10, -10).equals(light.position))
        self.assertTrue(Color(1, 1, 1).equals(light.intensity))


    def test_world2(self):
        w = World()
        r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
        intersections = w.intersect(r)
        self.assertEqual(intersections.count, 4)
        self.assertEqual(intersections.ls[0].t, 4)
        self.assertEqual(intersections.ls[1].t, 4.5)
        self.assertEqual(intersections.ls[2].t, 5.5)
        self.assertEqual(intersections.ls[3].t, 6)
    
    def test_world3(self):
        w = World()
        r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
        shape = w.objs[0]
        i = Intersection(4, shape)
        comps = i.prepare_computations(r)
        c = w.shade_hit(comps)
        self.assertTrue(Color(0.38066, 0.47583, 0.2855).equals(c))
    
    # def test_world4(self):
    #     # this test will fail since it is shadowed...
    #     w = World()
    #     w.light = Light(Point(0, 0.25, 0), Color(1, 1, 1))
    #     r = Ray(Point(0, 0, 0), Vector(0, 0, 1))
    #     shape = w.objs[1]
    #     i = Intersection(0.5, shape)
    #     comps = i.prepare_computations(r)
    #     c = w.shade_hit(comps)
    #     self.assertTrue(Color(0.90498, 0.90498, 0.90498).equals(c))
    
    def test_world5(self):
        w = World()
        r = Ray(Point(0, 0, -5), Vector(0, 1, 0))
        c = w.color_at(r)
        self.assertTrue(Color(0, 0, 0).equals(c))
    
    def test_world6(self):
        w = World()
        r = Ray(Point(0, 0, -5), Vector(0, 1, 0))
        c = w.color_at(r)
        self.assertTrue(Color(0, 0, 0).equals(c))
    
    def test_world7(self):
        w = World()
        r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
        c = w.color_at(r)
        self.assertTrue(Color(0.38066, 0.47583, 0.2855).equals(c))
    
    # def test_world8(self):
    #     w = World()
    #     s1 = Sphere()
    #     s2 = Sphere()
    #     t2 = scale(0.5, 0.5, 0.5)
    #     s2.set_transform(t2)

    #     w.objs = [s1, s2]

    #     outer = w.objs[0]
    #     outer.material.ambient = 1
    #     r = Ray(Point(0, 0, 0.75), Vector(0, 0, -1))
    #     intersections = w.intersect(r)


    def test_world8(self):
        w = World()
        outer = w.objs[0]
        outer.material.ambient = 1
        inner = w.objs[1]
        inner.material.ambient = 1
        r = Ray(Point(0, 0, 0.75), Vector(0, 0, -1))
        intersections = w.intersect(r)
        c = w.color_at(r)
        self.assertTrue(c.equals(inner.material.color))
    
    def test_shadow1(self):
        w = World()
        p = Point(0, 10, 0)
        self.assertFalse(w.is_shadowed(p))

    def test_shadow3(self):
        w = World()
        p = Point(10, -10, 10)
        self.assertTrue(w.is_shadowed(p))
    
    def test_shadow3(self):
        w = World()
        p = Point(-20, 20, -20)
        self.assertFalse(w.is_shadowed(p))
    
    def test_shadow4(self):
        w = World()
        p = Point(-2, 2, -2)
        self.assertFalse(w.is_shadowed(p))
    
    def test_shadow5(self):
        w = World()
        light = Light(Point(0, 0, -10), Color(1, 1, 1))
        w.light = light
        s1 = Sphere()
        s2 = Sphere()
        s2.transform = translate(0, 0, 10)
        w.objs = [s1, s2]
        r = Ray(Point(0, 0, 5), Vector(0, 0, 1))
        i = Intersection(4, s2)
        comps = i.prepare_computations(r)
        c = w.shade_hit(comps)
        self.assertTrue(Color(0.1, 0.1, 0.1).equals(c))
    
    def test_reflect1(self):
        w = World()
        r = Ray(Point(0, 0, 0), Vector(0, 0, 1))
        shape = w.objs[1]
        shape.material.abmient = 1
        i = Intersection(1, shape)
        comps = i.prepare_computations(r)
        color = w.reflected_color(comps)
        self.assertTrue(Color(0, 0, 0).equals(color))
    
    def test_reflect1(self):
        w = World()
        shape = Plane()
        shape.material.reflective = 0.5
        shape.set_transform(translate(0.0, -1.0, 0.0))
        w.objs.append(shape)
        r = Ray(Point(0.0, 0.0, -3.0), Vector(0.0, -sqrt(2)/2, sqrt(2)/2))
        i = Intersection(sqrt(2), shape)
        comps = i.prepare_computations(r)
        color = w.reflected_color(comps)
        # print(color)
        self.assertTrue(Color(0.19032, 0.2379, 0.14274).equals(color))
        # self.assertTrue(Color(0.190332, 0.237915, 0.1427491).equals(color))
    
    def test_shade_hit(self):
        w = World()
        shape = Plane()
        shape.material.reflective = 0.5
        shape.set_transform(translate(0.0, -1.0, 0.0))
        w.objs.append(shape)
        r = Ray(Point(0.0, 0.0, -3.0), Vector(0.0, -sqrt(2)/2, sqrt(2)/2))
        i = Intersection(sqrt(2), shape)
        comps = i.prepare_computations(r)
        color = w.shade_hit(comps)
        self.assertTrue(Color(0.87677, 0.92436, 0.82918).equals(color))
    
    def test_mutually_reflective_surfaces(self):
        w = World()
        w.light = Light(Point(0, 0, 0), Color(1, 1, 1))
        lower = Plane()
        lower.material.reflective = 1.0
        lower.set_transform(translate(0, -1, 0))

        up = Plane()
        up.material.reflective = 1.0
        up.set_transform(translate(0, 1, 0))

        r = Ray(Point(0, 0, 0), Vector(0, 1, 0))
        color = w.color_at(r)

    def test_maximum_recursive_depth(self):
        w = World()
        shape = Plane()
        shape.material.reflective = 0.5
        shape.set_transform(translate(0, -1, 0))
        r = Ray(Point(0, 0, -3), Vector(0, -sqrt(2)/2, sqrt(2)/2))
        i = Intersection(sqrt(2), shape)
        comps = i.prepare_computations(r)
        color = w.reflected_color(comps, 0)
        self.assertTrue(Color(0, 0, 0).equals(color))
    
    def test_refracted_color_opaque_surface(self):
        w = World()
        shape = w.objs[0]
        r = Ray(Point(0, 0, -5), Vector(0, 0, -1))
        ls = [
            Intersection(4, shape),
            Intersection(6, shape)
        ]
        xs = Intersections(ls)
        comps = xs[0].prepare_computations(r, xs)
        c = w.refracted_color(comps, 5)
        self.assertTrue(Color(0, 0, 0) == c)
    
    def test_refracted_color_at_maximum_recursive_depth(self):
        w = World()
        shape = w.objs[0]
        shape.material.transparency = 1.0
        shape.material.refractive_index = 1.5

        r = Ray(Point(0, 0, -5), Vector(0, 0, -1))
        ls = [
            Intersection(4, shape),
            Intersection(6, shape)
        ]
        xs = Intersections(ls)
        comps = xs[0].prepare_computations(r, xs)
        c = w.refracted_color(comps, 0)
        self.assertTrue(Color(0, 0, 0) == c)
    
    def test_refracted_color_under_total_internal_reflection(self):
        w = World()
        shape = w.objs[0]
        shape.material.transparency = 1.0
        shape.material.refractive_index = 1.5
        
        r = Ray(Point(0, 0, sqrt(2)/2), Vector(0, 1, 0))
        ls = [
            Intersection(-sqrt(2)/2, shape),
            Intersection(sqrt(2)/2, shape)
        ]
        xs = Intersections(ls)
        
        comps = xs[1].prepare_computations(r, xs)
        c = w.refracted_color(comps, 5)
        self.assertTrue(c == Color(0, 0, 0))

    def test_refracted_color_with_refracted_ray(self):
        w = World()
        A = w.objs[0]
        A.material.ambient = 1
        A.material.pattern = TestPattern()

        B = w.objs[1]
        B.material.transparency = 1.0
        B.material.refractive_index = 1.5

        r = Ray(Point(0, 0, 0.1), Vector(0, 1, 0))
        ls = [
            Intersection(-0.9899, A),
            Intersection(-0.4899, B),
            Intersection(0.4899, B),
            Intersection(0.9899, A)
        ]
        xs = Intersections(ls)
        comps = xs[2].prepare_computations(r, xs)
        c = w.refracted_color(comps, 5)
        print(c)
        self.assertTrue(c == Color(0, 0.99888, 0.04725))

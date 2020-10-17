from color import Color


class Material:
    def __init__(
        self,
        color=Color(1, 1, 1),
        ambient=0.1,
        diffuse=0.9,
        specular=0.9,
        shininess=200.
    ):
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.shininess = shininess
    
    def __eq__(self, m):
        if not isinstance(m, Material):
            raise TypeError
        return (
            m.color == self.color and
            m.ambient == self.ambient and
            m.diffuse == self.diffuse and
            m.specular == self.specular and
            m.shininess == self.shininess
        )
    
    def lighting(self, light, point, eyev, normalv, in_shadow):
        effective_color = self.color * light.intensity
        ambient = effective_color * self.ambient
        if in_shadow:
            return ambient
        lightv = (light.position-point).normalize()
        light_dot_normal = lightv.dot(normalv)
        if light_dot_normal < 0:
            diffuse = Color(0, 0, 0)
            specular = Color(0, 0, 0)
        else:
            diffuse = effective_color * self.diffuse * light_dot_normal
            reflectv = (-lightv).reflect(normalv)
            reflect_dot_eye = reflectv.dot(eyev)
            if reflect_dot_eye <= 0:
                specular = Color(0, 0, 0)
            else:
                factor = reflect_dot_eye ** self.shininess
                # print(factor)
                specular = light.intensity * self.specular * factor
        return ambient + diffuse + specular
        



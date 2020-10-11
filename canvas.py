from color import Color


class Canvas:
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.pixels = [[Color(0, 0, 0) for i in range(w)] for j in range(h)]
    
    def write_pixel(self, x, y, color):
        self.pixels[y][x] = color

    def pixel_at(self, x, y):
        return self.pixels[y][x]
    
    def to_ppm(self, fout):
        # setting maximum number of character each line to 70 is cumbersome. implement it later...
        # with open(fout, 'w') as outfile:
        fout.write("P3\n{} {}\n255".format(self.width, self.height))
        for j in range(self.height):
            fout.write('\n')
            for i in range(self.width):
                p = self.pixels[j][i]
                r = max(0, min(255, round(p.x*255)))
                g = max(0, min(255, round(p.y*255)))
                b = max(0, min(255, round(p.z*255)))
                fout.write("{} {} {} ".format(r, g, b))
        fout.write('\n')

            
import math

class RegularPolygon(object):
    def __init__(self, n):
        self.n = n
    
    def f(self):
        return self.n

    def g(self):
        return 0.5 * self.n * math.sin(2 * math.pi / self.n)
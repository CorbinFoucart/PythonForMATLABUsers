import numpy as np
import pdb

def sinkx(k,x):
    return np.sin(k*x)

class Shape(object):

    def __init__(self):
        pass

class Rectangle(Shape):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

class Square(Rectangle):

    def __init__(self, s):
        self.a = s
        self.b = s

    def __repr__(self):
        return 'Square\n side {}'.format(self.a)



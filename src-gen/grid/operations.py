import math

class Callback:
    def __init__(self):
        pass

    def abs_variable(self, val):
        return abs(val)

    def angle_diff(self, a, b):
        d = abs(a - b) % 360; 
        if d > 180:
            return 360 - d
        return d
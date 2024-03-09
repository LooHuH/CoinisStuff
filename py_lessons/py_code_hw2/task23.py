from askvar import askvar

x0 = 0
y0 = 0

cr1 = 4
cr2 = 6

class point:
    def __init__(self):
        self.x = askvar(f'point coordinate x')
        self.y = askvar(f'point coordinate y')
        self.r = (self.x**2 + self.y**2)**0.5
        self.is_below_the_line = _point_is_below_the_line()
        
    def _point_is_below_the_line(self):
        line_y = self.x - 4
        if self.y <= line_y:
            return True
        else:
            return False
        
point = Point()

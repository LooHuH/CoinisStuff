from askvar import askvar

x0 = 0
y0 = 0

cr1 = 4
cr2 = 6

class Point:
    def __init__(self):
        while True:
            self.x = askvar(f'point coordinate x')
            self.y = askvar(f'point coordinate y')
            
            if ((x0 - cr2 <= self.x <= x0 + cr2)
                    and (y0 - cr2 <= self.y <= y0 + cr2)):
                break
            
        self.r = (self.x**2 + self.y**2)**0.5
        
        line_y = self.x - 4
        if self.y <= line_y:
            self.is_below_the_line = True
        else:
            self.is_below_the_line = False
        
point = Point()

if (((point.x <= 0) and (point.y >= 0) and (cr1 <= point.r <= cr2))
        or ((point.x >= 0) and (point.y >= 0) and ((point.r <= cr1)
                                                   or ((cr1 <= point.r <= cr2) and point.is_below_the_line)))
        or ((point.x >= 0) and (point.y <= 0) and point.is_below_the_line)):
    print('Point is in ranges')
else:
    print('Point is not in ranges')
    

class Ellipse:
    def __init__(self, cx, cy, w, h, angle,minute) -> None:
        self.cx = cx
        self.cy = cy
        self.w = w
        self.h = h
        self.a = angle
        self.minute = minute

    def get_data(self):
        return [self.cx, self.cy, self.w, self.h, self.a,self.minute]

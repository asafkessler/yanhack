class Ellipse:
    def __init__(self, cx, cy, w, h) -> None:
        self.cx = cx
        self.cy = cy
        self.w = w
        self.h = h

    def get_data(self):
        return [self.cx, self.cy, self.w, self.h]

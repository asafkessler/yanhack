class Ellipse:
    def __init__(self, c1, c2, r) -> None:
        self.c1 = c1
        self.c2 = c2
        self.r = r

    def get_data(self):
        return [self.c1, self.c2, self.r]

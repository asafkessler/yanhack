class EllipseTime:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __eq__(self, o) -> bool:
        return o.start == self.start and o.end == self.end

    def __str__(self) -> str:
        return "["+str(self.start)+","+str(self.end)+"]"



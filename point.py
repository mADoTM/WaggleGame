from math import sqrt


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return 'x = ' + str(self.x) + ', y = ' + str(self.y)

    def distance(self, p2):
        return sqrt((p2.x - self.x) ** 2 + (p2.x - self.x))

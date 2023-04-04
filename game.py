from levelreader import LevelReader
from point import Point


class Game:
    def __init__(self, level_number):
        self.level = LevelReader.get_int_array_from_file(level_number)

    def do_step(self, p1, p2):
        if self.level[p2.y][p2.x] == 1 or self.level[p1.y][p1.x] == 0:
            return

        point_between = Point()
        if p1.x == p2.x:
            if abs(p2.y - p1.y) != 2:
                return
            point_between.x = p1.x
            point_between.y = min(p1.y, p2.y) + 1
        elif p1.y == p2.y:
            if abs(p2.x - p1.x) != 2:
                return
            point_between.x = min(p1.x, p2.x) + 1
            point_between.y = p1.y

        if self.level[point_between.y][point_between.x] == 0:
            return

        self.level[p1.y][p1.x] = 0
        self.level[point_between.y][point_between.x] = 0
        self.level[p2.y][p2.x] = 1

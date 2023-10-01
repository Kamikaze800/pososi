import math


class FlyingHouse:
    def __init__(self, height, speed, rooms=1):
        self.height = height
        self.speed = speed
        self.rooms = rooms

    def set_route(self, sp):
        self.sp = sp

    def print_route(self, v=1):
        if v == 0:
            return ''
        elif v > self.speed:
            v = self.speed
        dc = {'N': '↑', 'S': '↓', 'W': '←', 'E': '→'}
        res = ''
        for el in self.sp:
            res += dc[el[0]] * (int(el[1:]) // v)
        print(res)

    def change_height(self, val):
        self.height = self.height + val
        if self.height > 100:
            self.height = 100
        elif self.height < 0:
            self.height = 0

    def __str__(self):
        return f'{type(self).__name__}({self.height}, {self.speed}, {self.rooms})'


class FlyingCastle(FlyingHouse):
    def __init__(self, height, speed, titles, rooms=1):
        super().__init__(height, speed, rooms)
        self.titles = titles

    def __add__(self, other):
        if isinstance(other, FlyingCastle):
            height = min(self.height, other.height)
            speed = math.floor((self.speed + other.speed) / 2)
            titles = self.titles + other.titles
            rooms = len(titles)
            return FlyingCastle(height, speed, titles, rooms)
        elif isinstance(other, str):
            self.titles.append(other)
            self.rooms = len(self.titles)
            return self

    def __str__(self):
        return f'{type(self).__name__}({self.height}, {self.speed}, {self.titles}, {self.rooms})'

    def __repr__(self):
        return f'{type(self).__name__}({self.height}, {self.speed}, {self.titles}, {self.rooms})'

    def __lt__(self, other):
        if self.rooms == other.rooms:
            if self.height == other.height:
                return self.speed < other.speed
            return self.height < other.height
        return self.rooms < other.rooms

    def __le__(self, other):
        if self.rooms == other.rooms:
            if self.height == other.height:
                return self.speed <= other.speed
            return self.height < other.height
        return self.rooms < other.rooms

    def __eq__(self, other):
        if self.rooms == other.rooms:
            if self.height == other.height:
                return self.speed == other.speed
            return False
        return False

    def __ne__(self, other):
        if self.rooms == other.rooms:
            if self.height == other.height:
                return self.speed != other.speed
            return True
        return True

    def __gt__(self, other):
        if self.rooms == other.rooms:
            if self.height == other.height:
                return self.speed > other.speed
            return self.height > other.height
        return self.rooms > other.rooms

    def __ge__(self, other):
        if self.rooms == other.rooms:
            if self.height == other.height:
                return self.speed >= other.speed
            return self.height > other.height
        return self.rooms > other.rooms

fc = FlyingCastle(29, 15, ['sauna', 'cinema', 'kitchen', 'library'], 4)
fc.set_route(['W39', 'W54', 'W67', 'E49', 'E17', 'S22', 'E63'])
fc.print_route(0)
fc += 'bathroom'
fc1 = FlyingCastle(24, 25, ['bathroom', 'kitchen', 'banquet hall', 'bedroom', 'sauna', 'living room'], 6)
print(fc, fc1, sep='\n')
fc2 = fc + fc1
print(fc, fc1, fc2, sep='\n')
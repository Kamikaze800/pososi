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

class FlyingCity:
    def __init__(self, sp):
        self.sp = sp

    def collect(self, condition):
        return FlyingCity(filter(condition, self.sp))

    def __getitem__(self, key):
        return self.sp[key]

    def __setitem__(self, key, value):
        self.sp[key] = value

    def __len__(self):
        return len(self.sp)

    def append(self, val):
        self.sp.append(val)

    def extend(self, val):
        self.sp.extend(val)

    def pop(self, key):
        return self.sp.pop(key)
    def __delitem__(self, key):
        return self.sp.pop(key)

    def __iadd__(self, other):
        self.sp += other
        return self



fc = FlyingCastle(29, 11, ['sauna', 'library'], 2)
fh = FlyingHouse(9, 23)
city = FlyingCity([fc, fh])
city += [FlyingHouse(31, 16)]
city.append(FlyingCastle(5, 16, ['gym'], 1))
print(city)
city1 = FlyingCity([FlyingCastle(22, 6, ['cinema', 'banquet hall'], 2),
                    FlyingHouse(29, 23)])
print(city1)
print(city1.pop())
print(len(city1))

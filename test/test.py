class FlyingHouse:
    def __init__(self, height, speed, rooms=1):
        self.height = height
        self.speed = speed
        self.rooms = rooms

    def set_route(self, route):
        self.route = route

    def print_route(self, v=1):
        dic = {'W': '←', 'N': '↑', 'S': '↓', 'E': '→'}
        path = []
        if v > self.speed:
            v = self.speed
        if not v:
            print()
        else:
            for item in self.route:
                path.append(dic[item[0]] * (int(item[1:]) // v))
            print(''.join(path))

    def change_height(self, value):
        if self.height + value > 100:
            self.height = 100
        elif self.height + value < 0:
            self.height = 0
        else:
            self.height += value

    def _str_(self):
        return f"{self.__class__.__name__}({self.height}, {self.speed}, {self.rooms})"


class FlyingCastle(FlyingHouse):
    def __init__(self, height, speed, titles, rooms=1):
        super().__init__(height, speed, rooms)
        self.titles = titles

    def __add__(self, other):
        height = min(self.height, other.height)
        speed = int((self.speed + other.speed) / 2)
        rooms = self.rooms + other.rooms
        titles = self.titles[:] + other.titles[:]
        return FlyingCastle(height, speed, titles, rooms)

    def __str__(self):
        return f"{self.__class__.__name__}({self.height}, {self.speed}, {self.titles}, {self.rooms})"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.height}, {self.speed}, {self.titles}, {self.rooms})"

    def __iadd__(self, other):
        self.titles.append(other)
        self.rooms += 1
        return self

    def __le__(self, other):
        return (self.rooms, self.height, self.speed) <= (
            other.rooms, other.height, other.speed
        )

    def __gt__(self, other):
        return (self.rooms, self.height, self.speed) > (
            other.rooms, other.height, other.speed
        )

    def __eq__(self, other):
        return (self.rooms, self.height, self.speed) == (
            other.rooms, other.height, other.speed
        )

fc = FlyingCastle(29, 15, ['sauna', 'cinema', 'kitchen', 'library'], 4)
fc.set_route(['W39', 'W54', 'W67', 'E49', 'E17', 'S22', 'E63'])
fc.print_route(0)
fc += 'bathroom'
fc1 = FlyingCastle(24, 25, ['bathroom', 'kitchen', 'banquet hall', 'bedroom', 'sauna', 'living room'], 6)
print(fc, fc1, sep='\n')
fc2 = fc + fc1
print(fc, fc1, fc2, sep='\n')

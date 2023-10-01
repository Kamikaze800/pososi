import itertools
class Parallel:
    def __init__(self, lessons):
        self.lessons = lessons
        classes = [list(self.lessons.keys)[:3]]
        proverka = 0
        while len(classes) < 3:
            for les in classes[proverka]:
                lessons[les] -= 1
            proverka += 1
            lessons = {x: lessons[x] for x in lessons.keys() if lessons[x] > 0}
            

        print(classes)


a = Parallel({'рус': 3, 'мат': 6, 'ист': 2, 'общ': 2})
# b = Parallel({'рус': 3, 'мат': 6, 'ист': 2, 'икт': 5, 'физ': 6, 'общ': 2, 'англ': 2, 'фир-ра': 2})

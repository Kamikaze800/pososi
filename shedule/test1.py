import itertools
import random


class Parallel:
    def __init__(self, **classes):
        self.lessons = lessons
        for day in range(5):
            classes = []
            res_variants = []
            variants = [[x] * self.lessons[x] for x in self.lessons.keys()]
            for el in variants:
                res_variants.extend(el)
            random.shuffle(res_variants)
            # print(res_variants)
            begin = 0
            end = 5
            while end != 25:
                classes.append(res_variants[begin: end])
                begin += 5
                end += 5
            classes[0]
            print(classes)



a = Parallel({'рус': 3, 'мат': 6, 'ист': 2, 'общ': 2, 'физ': 6}, {'рус': 6, 'мат': 3, 'ист': 5, 'общ': 4, 'физ': 1, 'право': 2})
# b = Parallel({'рус': 3, 'мат': 6, 'ист': 2, 'икт': 5, 'физ': 6, 'общ': 2, 'англ': 2, 'фир-ра': 2})
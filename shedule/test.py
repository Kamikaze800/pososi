import itertools


class Parallel:
    def __init__(self, lessons):
        self.lessons = lessons
        classes = []
        variants = list(itertools.permutations(self.lessons.keys()))
        for class_number in range(len(variants)):
            if class_number == 0:
                classes.append(variants[0])
                for les in variants[0]:
                    self.lessons[les] -= 1

            else:
                points = 0
                for les_class_num in range(len(classes)):
                    for lesson_number in range(len(variants[class_number])):
                        if variants[class_number][lesson_number] == classes[les_class_num][lesson_number]:
                            break
                        if self.lessons[variants[class_number][lesson_number]] == 0:
                            break
                        elif lesson_number == len(classes[les_class_num]) - 1:
                            points += 1
                if points == len(classes):
                    classes.append(variants[class_number])

        print(classes)


a = Parallel({'рус': 3, 'мат': 6, 'ист': 2, 'общ': 2})
# b = Parallel({'рус': 3, 'мат': 6, 'ист': 2, 'икт': 5, 'физ': 6, 'общ': 2, 'англ': 2, 'фир-ра': 2})

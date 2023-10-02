import itertools
import math
import random


class Parallel:
    def __init__(self, *classes):
        res = []
        mid_count = 4 # среднее кол-во уроков в день
        for i in range(5):
            shedule_day = []  # расписание на день для всех
            for klass in classes:
                shedule_klass = []  # расписание для класса
                ind = 0  # номер урока
                big_les = [x for x in klass.keys() if klass[x] > 3] # если уроков больше 2
                points = 1 # кол-во предмета в день
                for les in klass.keys():
                    if les in big_les:
                        points = 2
                    for j in range(points):
                        if klass[les] > 0 and len(shedule_klass) < mid_count:  # проеряем, что кол-во часов для предмета больше 0
                            les_ind = []  # уроки классов по номеру.
                            for x in shedule_day:
                                # добавлем только те классы, чьё расписание больше или равно нынешнему номеру урока
                                if len(x) > ind:
                                    les_ind.append(x[ind])
                            # если нынешний урок не совпадает с уроками по этому же номеру в параллели - добавляем
                            if les not in les_ind:
                                shedule_klass.append(les)
                                klass[les] -= 1
                                ind += 1
                    points = 1
                shedule_day.append(shedule_klass)
            res.append(shedule_day)
        for i in res:
            print(i)


a = Parallel({'рус': 3, 'мат': 6, 'ист': 2, 'общ': 2, 'физ': 6, 'англ': 6},
             {'рус': 6, 'мат': 3, 'ист': 5, 'общ': 4, 'физ': 1, 'право': 2},
             {'рус': 3, 'мат': 3, 'ист': 2, 'общ': 2, 'физ': 1, 'хим': 5, 'биол': 4})
# b = Parallel({'рус': 3, 'мат': 6, 'ист': 2, 'икт': 5, 'физ': 6, 'общ': 2, 'англ': 2, 'фир-ра': 2})

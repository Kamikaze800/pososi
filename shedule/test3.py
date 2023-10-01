import itertools
import random


class Parallel:
    def __init__(self, *classes):
        res = []
        for i in range(5):
            shedule_day = []  # расписание на день для всех
            for klass in classes:
                shedule_klass = []  # расписание для класса
                ind = 0  # номер урока
                mid_count = round(sum(klass.values()) / len(klass)) # среднее кол-во уроков в день
                big_les = {x: y for x, y in klass if y > 2} # если уроков больше 2
                points = 1 # кол-во предмета в день
                for les in klass.keys():
                    if les in big_les:
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
                print(shedule_day)


a = Parallel({'рус': 3, 'мат': 6, 'ист': 2, 'общ': 2, 'физ': 6},
             {'рус': 6, 'мат': 3, 'ист': 5, 'общ': 4, 'физ': 1, 'право': 2})
# b = Parallel({'рус': 3, 'мат': 6, 'ист': 2, 'икт': 5, 'физ': 6, 'общ': 2, 'англ': 2, 'фир-ра': 2})
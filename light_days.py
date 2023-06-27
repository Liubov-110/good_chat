import random
from prettytable import PrettyTable
from days_detailed import week, day_night_parts
from days_detailed import suggestions



def fill_timetable():
    timetable = PrettyTable()
    timetable.title = 'Will any electricity be present?'
    timetable.field_names = ['Era part', 'Time frame', *week]
    timetable.align['Era part'] = 'l'
    for p in day_night_parts.keys():
        r7 = []
        for _ in range(7):
            r = random.choice(['Yes', 'No', 'unknown'])
            r7.append(r)
        timetable.add_row([p, day_night_parts[p][0], *r7])
    return timetable

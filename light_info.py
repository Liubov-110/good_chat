import days_detailed
import light_days
from days_detailed import suggestions


def show_full_el_info():
    lt = light_days.fill_timetable()
    print(lt)


def show_info_1day(d):
    lt_s = light_days.fill_timetable()
    lt_s.add_column('To do', suggestions)
    lt_s.title = 'Electricity?'
    lt_s.align['To do'] = 'r'
    d = days_detailed.week[d-1]
    st = lt_s.get_string(fields=['Era part', d, 'To do'])
    print(st)


def show_info_hours(d, h, h_r=1):
    lt_s = light_days.fill_timetable()
    lt_s.add_column('To do', suggestions)
    lt_s.title = 'Electricity?'
    lt_s.align['To do'] = 'r'
    d = days_detailed.week[d - 1]
    ht = lt_s.get_string(fields=['Era part', d, 'To do'], start=h//4, end=(h+h_r)//4 + 1)
    print(ht)

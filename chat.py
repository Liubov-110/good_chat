import light_info
import datetime
import art
from tqdm import tqdm
from time import sleep
from days_detailed import suggestions, added_todos


def greeting():
    print('Привіт! Цей чат є написаний мовою Python')


def regards():
    art.tprint('Have a nice day!', font='wiz')


def menu():
    try:
        chosen_action = int(input('Чат вміє:\n'
                              '\t0 - познайомитись\n'
                              '\t1 - показати розклад дня\n'
                              '\t2 - показати розклад на тиждень\n'
                              '\t3 - інформувати про наявність електроенергії\n'
                              '\t4 - додати нові активності до переліку справ\n'
                              '\t9 - завершити розмову\n'))
    except ValueError:
        print('Наступного разу робіть свій вибір уважніше. Програма розуміє лише цифри. Все інше ми перетворюємо на 0')
    else:
        match chosen_action:
            case 9: return 'quit'
            case 4: add_new_todo()
            case 3: ask_full_or_1day()
            case 2: show_weekly_todo_list()
            case 1: show_daily_todo_list()
            case 0: greeting()
            case _: print('Програма не зрозуміла Вашого вибору')



def add_new_todo():
    todo = input('Що бажаєте записати до переліку важливих справ: ')
    added_todos.append(todo)
    for i in tqdm(range(3), total=3, ncols=110, desc='Зберігаємо введену інформацію...', colour='green'):
        sleep(i)


def show_daily_todo_list():
    print('Основний список важливих справ на день:')
    print(*suggestions, sep='\n')
    if added_todos:
        print('\nА також в додатковому списку є таке:', *added_todos, sep='\n')
    print('\nThis feature is in development phase right now and full functionality will be available after next release')


def show_weekly_todo_list():
    print('Основний список важливих справ на кожен день тижня:')
    print(*suggestions, sep='\n')
    if added_todos:
        print('\nА також в додатковому списку є таке:', *added_todos, sep='\n')
    print('\nThis feature is in development phase right now and full functionality will be available after next release')


def ask_full_or_1day():
    sel_range = int(input('Оберіть будь ласка для якого періоду часу розклад наявності е/е Вас цікавить\n'
                      '\t0 - весь відомий розклад\n'
                      '\t1 - на сьогодні\n'
                      '\t2 - на інший день\n'
                      '\t3 - зараз\n'
                      '\t4 - інший період протягом одного дня\n'))
    match sel_range:
        case 0: light_info.show_full_el_info()
        case 1: light_info.show_info_1day(datetime.date.today().isoweekday())
        case 2:
            sel_day = int(input('Введіть номер дня від 1 до 7 '))    # input check needed or some try_catch clause, or even separate function as its also present in case 4, line 77
            light_info.show_info_1day(sel_day)
        case 3:
            light_info.show_info_hours(datetime.date.today().isoweekday(), datetime.datetime.now().hour)
        case 4:
            sel_day = int(input('Введіть номер дня від 1 до 7 '))
            sel_hour_start = int(input('Введіть початкову годину періоду, що Вас цікавить '))
            sel_hour_range = int(input('Яка тривалість вибраного періоду? '))
            if sel_hour_start + sel_hour_range > 24:
                sel_hour_range = 24 - sel_hour_start
            light_info.show_info_hours(sel_day, sel_hour_start, sel_hour_range)
        case _:
            print('Програма не зрозуміла Вашого вибору')

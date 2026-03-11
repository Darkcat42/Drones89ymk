from flask_admin.contrib.peewee import ModelView
class Schedule_admin(ModelView):
    list_template = 'admin/tables/schedule.html'
    # загружаем в объект представления flask-admin данные для меню панели администраора
    def __init__(self, model, *args, **kwargs):
        if 'name' not in kwargs:
            kwargs['name'] = 'Расписание'
        super().__init__(model, *args, **kwargs)
    # форматируем сами столбцы
    column_labels = {
        'location' : 'Локация',
        'day' : 'День недели',
        'start' : 'начало занятий',
        'end' : 'конец занятий',
    }

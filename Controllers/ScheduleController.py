from Models.Schedule import *
class ScheduleController():
    """
        управление данными таблицы расписание
    """
    @classmethod
    def addDay(cls, location, day, start, end):
        Schedule.create(
            location=location,
            day=day,
            start=start,
            end=end
        )
    @classmethod
    def get(cls):
        return Schedule.select()
    @classmethod
    def show(cls, id):
        return Schedule.get_or_none(Schedule.id == id)
    @classmethod
    def delete(cls, id):
        return Schedule.delete().where(Schedule.id == id).execute()
    @classmethod
    def update(cls, id, **filds):
        for key, value in filds.items():
            Schedule.update({key:value}).where(Schedule.id == id).execute()
    @classmethod
    def showLast(cls):
        return Schedule.select().order_by(Schedule.id.desc()).get()
    
    @classmethod
    def get_currentScheduleDay(cls, id):
        day = ScheduleController.show(id)
        day_dict = {}
        day_dict['id'] = day.id
        day_dict['location'] = day.location
        day_dict['day'] = day.day
        day_dict['start'] = day.start
        day_dict['end'] = day.end
        return day_dict
    @classmethod
    def get_ScheduleDays(cls):
        """
        метод для перебора объекта в массив
        для передачи его в шаблонизатор внутри
        html
        :return: массив строк таблицы time_table"""
        schedule = cls.get()
        scheduleDays = []
        for day in schedule:
            day_dict = {}
            day_dict['id'] = day.id
            day_dict['location'] = day.location
            day_dict['day'] = day.day
            day_dict['start'] = day.start
            day_dict['end'] = day.end
            scheduleDays.append(day_dict)
        return scheduleDays
    # @classmethod
    # def get_by_login(cls, search_login):
    #     return Users.get_or_none(Users.login==search_login)
    # @classmethod
    # def show(cls, id):
    #     return Users.get_or_none(id)
    # @classmethod
    # def update(cls, id, **filds):
    #     for key, value in filds.items():
    #         Users.update({key:value}).where(Users.id == id).execute()
    # @classmethod
    # def delete(cls, id):
    #     Users.delete().where(Users.id == id).execute()
if __name__ == '__main__':
    print(ScheduleController.get_ScheduleDays())
    # Time_tableController.add(
    #     title='Расписание',
    #     location='спорт комплекс ЯМК 2 зал',
    #     day='Понедельник',
    #     start='16:00',
    #     end='18:00',
    #     requirements='требования - иметь сменную обувь',
    #     description='расписание наших занятий'
    # )
    # Time_tableController.add(
    #     title='',
    #     location='ОТП ЯМК 216 кабинет второй этаж',
    #     day='вторник',
    #     start='16:00',
    #     end='18:00',
    #     requirements='',
    #     description=''
    # )





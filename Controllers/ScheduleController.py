from Models.Schedule import Schedule
from Controllers.ModelsController import ModelsController
class ScheduleController(ModelsController):
    """управление данными расписания"""
    model = Schedule
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
        :return: массив строк таблицы"""
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




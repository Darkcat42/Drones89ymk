
from Models.time_table import *
class Time_tableController():
    @classmethod
    def add(cls, title, location, day, start, end, requirements, description):
        time_table.create(
            title=title,
            location=location,
            day=day,
            start=start,
            end=end,
            requirements=requirements,
            description=description
        )
    @classmethod
    def get(cls):
        return time_table.select()
    @classmethod
    def get_table_rows(cls):
        """:return: массив строк таблицы time_table"""
        table_obj = Time_tableController.get()
        rows_mass = []
        for row in table_obj:
            check = True
            while check == True:
                new_row = {}
                new_row['title'] = row.title
                new_row['location'] = row.location
                new_row['day'] = row.day
                new_row['start'] = row.start
                new_row['end'] = row.end
                new_row['requirements'] = row.requirements
                new_row['description'] = row.description
                rows_mass.append(new_row)
                check = False
        return rows_mass
    
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
    Time_tableController.add(
        title='Расписание',
        location='спорт комплекс ЯМК 2 зал',
        day='Понедельник',
        start='16:00',
        end='18:00',
        requirements='требования - иметь сменную обувь',
        description='расписание наших занятий'
    )
    Time_tableController.add(
        title='',
        location='ОТП ЯМК 216 кабинет второй этаж',
        day='вторник',
        start='16:00',
        end='18:00',
        requirements='',
        description=''
    )





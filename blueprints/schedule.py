# импорты системных библиотек
import flask, os, datetime
from flask_login import login_required
from flask import render_template, request, Blueprint, current_app
from Controllers.ScheduleController import ScheduleController

schedule_blueprint = Blueprint('schedule', __name__)
# маршруты для блока расписания главной страницы
@schedule_blueprint.route('/updateSchedule_page/<id>', methods=['GET'])
@login_required
def updateSchedule_page(id):
        return flask.render_template(
            'schedule/updateSchedule_action.html',
            day = ScheduleController.get_currentScheduleDay(id)
        )
@schedule_blueprint.route('/updateSchedule_action/<id>', methods=['POST'])
@login_required
def updateScheduleDay(id):
    if request.method == "POST":
        day_id = id
        ScheduleController.update(
            day_id, 
            location = request.form.get('location'),
            day = request.form.get('day'),
            start = request.form.get('start'),
            end = request.form.get('end')
            )
        return flask.redirect('/admin_panel#schedule')

@schedule_blueprint.route('/createSchedule_page', methods=['GET'])
@login_required # переделать!
def redirect_to_createSchedule_page():
    return flask.redirect('/createSchedule_page/create')
@schedule_blueprint.route('/createSchedule_page/<msg>', methods=['GET'])
@login_required
def createSchedule_page(msg):
        return flask.render_template(
            'schedule/createSchedule_action.html',
            edit_schedule = False,
            day = None,
            msg = msg
        )
@schedule_blueprint.route('/createSchedule_action', methods=['POST'])
@login_required
def createScheduleDay():
    if request.method == "POST":
        location = request.form.get('location')
        day = request.form.get('day')
        start = request.form.get('start')
        end = request.form.get('end')
        if location == '' or day == '' or start == '' or end == '':
            return flask.redirect('/createSchedule_page/Заполните поля!')
        try:
            ScheduleController.addDay(
                location=location,
                day=day,
                start=start,
                end=end
            )
        except:
            return 'ошибка при работе с базой данных'
        current_day = ScheduleController.showLast() 
        current_day = {
            'id' : current_day.id,
            'day' : current_day.day,
            'start' : current_day.start,
            'end' : current_day.end,
            'location' : current_day.location
        }
        return flask.redirect('/admin_panel#schedule')
@schedule_blueprint.route('/deleteScheduleDay/<id>', methods=['GET'])
@login_required
def deleteScheduleDay(id):
    result = ScheduleController.delete(id=id)
    return flask.redirect('/admin_panel#schedule')
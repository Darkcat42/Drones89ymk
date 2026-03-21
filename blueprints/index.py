# импорты системных библиотек
import flask, os, datetime
from flask_login import login_required
from flask import render_template, request, Blueprint, current_app
from Controllers.ScheduleController import ScheduleController
from Controllers.NewsController import NewsController
from Controllers.SlidersController import SlidersController

index_blueprint = Blueprint('index_bluep', __name__)
@index_blueprint.route('/') 
def index():
    """маршрут на главную"""
    try:
        slider = SlidersController.get_by_attr('name', 'drones')
    except:
        slider = None
    return render_template(
        'index/index.html',
        scheduleDays=ScheduleController.get(),
        scheduleInfo='[расписание]',
        news=NewsController.get_desc(),
        slider = slider
        )
@index_blueprint.route('/flask_admin/')
@login_required
def flask_admin():
    return flask.redirect('/admin/')
# маршруты для страницы документов с правилами
@index_blueprint.route('/doc')
def doc():
    """маршрут страницу документов"""
    return render_template('doc.html')
# маршруты для страницы политики обработки персональных данных
@index_blueprint.route('/policy')
def policy():
    """маршрут policy.html"""
    return render_template('policy.html')


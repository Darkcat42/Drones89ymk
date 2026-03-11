# импорты системных библиотек
import flask, os, datetime
from flask_login import login_required
from flask import render_template, request, Blueprint, current_app
from Controllers.ScheduleController import ScheduleController
from Controllers.NewsController import NewsController

index_blueprint = Blueprint('index_blueprint', __name__)
@index_blueprint.route('/') 
def index():
    """маршрут на главную"""
    return render_template(
        'main/index.html',
        scheduleDays=ScheduleController.get_ScheduleDays(),
        scheduleInfo='[расписание]',
        lastNews=NewsController.getLast_dict()
        )
@index_blueprint.route('/admin_panel')
@login_required
def admin_panel():
    return render_template(
        'main/admin_panel.html',
        scheduleDays=ScheduleController.get_ScheduleDays(),
        scheduleInfo='расписание',
        lastNews=NewsController.getLast_dict()
        )
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


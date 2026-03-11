# импорты системных библиотек
import flask, os, datetime
from flask_login import login_required
from flask import render_template, request, Blueprint, current_app
from Controllers.HardwaresController import HardwaresController
from pathlib import Path

hardwares_blueprint = Blueprint('hardwares', __name__) 


# маршруты для страницы оборудования
@hardwares_blueprint.route('/hardwares')
@login_required
def hardwares():
    """маршрут на страницу """
    return render_template(
        'hardwares/hardwares.html',
        hardwares = HardwaresController.get_hardwares()
        )
@hardwares_blueprint.route('/createHardwares_page', methods=['GET']) 
@login_required
def createHardwares_page():
    return flask.render_template(
        'hardwares/createHardwares_page.html',
       
        )
@hardwares_blueprint.route('/createHardwares_action', methods=['POST']) 
@login_required
def createHardwares_action():
    if request.method == "POST":
        cat = request.form.get('cat')
        name = request.form.get('name')
        
        cost = request.form.get('cost')
        count = request.form.get('count')
        sourceName = request.form.get('sourceName')
        sourceUrl = request.form.get('sourceUrl')
    hardware = HardwaresController.add(
        category = cat,
        name = name,
        
        cost = cost,
        count = count,
        sourceName = sourceName,
        sourceUrl = sourceUrl
    )
    return flask.redirect('/hardwares')
@hardwares_blueprint.route('/updateHardwares_action/<id>', methods=['POST']) 
@login_required
def updateHardwares_action(id):
    if request.method == "POST":
        name = request.form.get('name')
        cost = request.form.get('cost')
        count = request.form.get('count')
        sourceName = request.form.get('sourceName')
        sourceUrl = request.form.get('sourceUrl')
    hardware = HardwaresController.update(
        id,
        name = name,
        cost = cost,
        count = count,
        sourceName = sourceName,
        sourceUrl = sourceUrl
    )
    return flask.redirect('/hardwares')
@hardwares_blueprint.route('/updateHardwares_page/<id>', methods=['GET']) 
@login_required
def updateHardwares_page(id):
    return flask.render_template(
        'hardwares/updateHardwares_page.html',
        hardware = HardwaresController.get_cur_hardware(id)
        )
@hardwares_blueprint.route('/deleteHardwares_action/<id>', methods=['GET']) 
@login_required
def deleteHardwares_action(id):
    HardwaresController.delete(id)
    return flask.redirect('/hardwares')
# импорты системных библиотек
import flask, os, datetime
from flask_login import login_required
from flask import render_template, request, Blueprint, current_app
from Controllers.BuildController import BuildController
from Controllers.HardwaresController import HardwaresController
from Controllers.PersonsController import PersonsController
from Controllers.Builds_hardwaresController import Builds_hardwaresController
from Controllers.Builds_authorsController import Builds_authorsController
from Controllers.ImagesController import ImagesController
from pathlib import Path

builds_blueprint = Blueprint('builds', __name__) 


# маршруты для страницы сборок
@builds_blueprint.route('/build')
def build():
    """маршрут на страницу сборок с дронами"""
    return render_template(
        'builds/build.html',
        builds = BuildController.getBuilds()
        )
@builds_blueprint.route('/createBuilds_page', methods=['GET']) 
@login_required
def createBuilds_page():
    hardwares = []
    hardwares.append(['Рамы', HardwaresController.get_hardwaresCategoty('frames')])
    hardwares.append(['Периферия', HardwaresController.get_hardwaresCategoty('periphery')])
    hardwares.append(['Полетные контроллеры', HardwaresController.get_hardwaresCategoty('flighters')])
    hardwares.append(['Двигатели', HardwaresController.get_hardwaresCategoty('engines')])
    hardwares.append(['Расходники', HardwaresController.get_hardwaresCategoty('consumables')])
    hardwares.append(['Программное обеспечение', HardwaresController.get_hardwaresCategoty('software')])
    return flask.render_template(
        'builds/createBuilds_page.html',
        hardwares = hardwares,
        persons = PersonsController.getPersons(),
        )
@builds_blueprint.route('/createBuilds_action', methods=['POST']) 
@login_required
def createBuilds_action():
    if request.method == "POST":
        file = request.files['file'] 
        try:
            filename = file.filename
            dir_name = current_app.appСontorller.make_categoryDir('builds')
            if Path(filename).suffix != '.webp':
                fileSrc = os.path.join(current_app.appСontorller.tempImg, filename)
                file.save(fileSrc) # сохраняем файл во временную папку
                webp_src = ImagesController.convertImage(fileSrc, dir_name) 
                filename = str(Path(filename).stem)+'.webp'
            else:
                webp_src = os.path.join(dir_name, filename) 
                file.save(webp_src)
            image = ImagesController.add(
                filename=filename,
                src=webp_src)
            image_id = image.id
        except:
            image_id = ImagesController.get()[0].id
        inch = request.form.get('inch')
        build_desc = request.form.get('build_desc')
        author_id = request.form.get('author')
        hardwares_id = request.form.getlist('hardwares_id')
        builds = BuildController.add(
            inch = inch,
            build_desc = build_desc,
            build_image_id = image_id
        )
        for id in hardwares_id:
            Builds_hardwaresController.add(
                Hardwares_id = id,
                builds_id = builds.id
            )
        Builds_authorsController.add(
            persons_id = author_id,
            builds_id = builds.id
        )
        return flask.redirect('/build')
@builds_blueprint.route('/updateBuilds_action/<id>', methods=['POST']) 
@login_required
def updateBuilds_action(id):
    if request.method == "POST":
        file = request.files['file']
        # file = request.files('file') 
        try:
            # file = request.files.getlist('file') # множественная загрузка
            filename = file.filename
            dir_name = current_app.appСontorller.make_categoryDir('builds')
            if Path(filename).suffix != '.webp':
                fileSrc = os.path.join(current_app.appСontorller.tempImg, filename)
                file.save(fileSrc) # сохраняем файл во временную папку
                
                webp_src = ImagesController.convertImage(fileSrc, dir_name) 
                filename = str(Path(filename).stem)+'.webp'
            else:
                webp_src = os.path.join(dir_name, filename) 
                file.save(webp_src)
            image = ImagesController.add(
                filename=filename,
                src=webp_src)
            image_id = image.id
        except:
            image_id = ImagesController.get()[0].id
        inch = request.form.get('inch')
        build_desc = request.form.get('build_desc')
        builds = BuildController.add(
            name = inch,
            cost = build_desc,
            build_image_id = image_id
        )
        return flask.redirect('/build')
@builds_blueprint.route('/updateBuilds_page/<id>', methods=['GET']) 
@login_required
def updateBuilds_page(id):
    return flask.render_template(
        'builds/updateBuilds_page.html',
        hardware = HardwaresController.get_cur_hardware(id)
        )
@builds_blueprint.route('/deleteBuilds_action/<id>', methods=['GET']) 
@login_required
def deleteBuilds_action(id):
    BuildController.delete(id)
    return flask.redirect('/build')
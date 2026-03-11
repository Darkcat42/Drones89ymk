# импорты системных библиотек
import flask, os, datetime
from flask_login import login_required
from flask import render_template, request, Blueprint, current_app
from Controllers.PersonsController import PersonsController
from Controllers.ImagesController import ImagesController
from pathlib import Path

persons_blueprint = Blueprint('persons_bluep', __name__) 

# маршруты для страницы персон
@persons_blueprint.route('/persons')
def persons():
    """маршрут на страницу """
    return render_template(
        'persons/persons.html',
        persons = PersonsController.getPersons()
        )
@persons_blueprint.route('/createPersons_page', methods=['GET']) 
@login_required
def createPerson_page():
    return flask.render_template(
        'persons/createPersons_page.html'
        )
@persons_blueprint.route('/createPersons_action', methods=['POST']) 
@login_required
def createPersons_action():
    if request.method == "POST":
        persons_types_id = request.form.get('persons_types_id')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        person_desc = request.form.get('person_desc')
        file = request.files['file']
    try:
        filename = file.filename
        dir_name = current_app.appСontorller.make_categoryDir('persons')
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
    person = PersonsController.add(
        persons_types_id = persons_types_id,
        images_id = image_id,
        firstName = firstName,
        lastName = lastName,
        person_desc = person_desc
    )
    return flask.redirect('/persons')

@persons_blueprint.route('/updatePerson_action/<id>', methods=['POST']) 
@login_required
def updatePersons_action(id):
    if request.method == "POST":
        file = request.files.getlist('file') # множественная загрузка
        try:
            file = request.files.getlist('file') # множественная загрузка
            filename = file.filename
            dir_name = current_app.appСontorller.make_categoryDir('persons')
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
        person = PersonsController.update(
            id,
            persons_types_id = request.form.get('persons_types_id'),
            images_id = image_id,
            firstName = request.form.get('firstName'),
            lastName = request.form.get('lastName'),
            person_desc = request.form.get('person_desc')
        )
    return flask.redirect('/persons')
@persons_blueprint.route('/updatePersons_page/<id>', methods=['GET']) 
@login_required
def updatePerson_page(id):
    return flask.render_template(
        'persons/updatePersons_page.html',
        person = PersonsController.get_cur_Person(id)
        )
@persons_blueprint.route('/deletePersons_action/<id>', methods=['GET']) 
@login_required
def deletePersons_action(id):
    PersonsController.delete(id)
    return flask.redirect('/persons')
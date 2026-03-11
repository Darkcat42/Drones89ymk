# импорты системных библиотек
import flask, os, datetime
from flask_login import login_required
from flask import render_template, request, Blueprint, current_app
from Controllers.GalleryEventsController import GalleryEventsController
from Controllers.GalleryEvents_imagesController import GalleryEvents_imagesController
from Controllers.ImagesController import ImagesController
from pathlib import Path

gallery_blueprint = Blueprint('gallery', __name__) 

# маршруты для страницы галерея
@gallery_blueprint.route('/gallery') 
def gallery():
    """маршрут на страницу с галереей"""
    return render_template(
        'gallery/gallery.html',
        list_of_gallerys = GalleryEvents_imagesController.get_all_gallerys()
        )
@gallery_blueprint.route('/deleteGalleryEvent_page/<id>', methods=['GET']) 
@login_required
def deleteGalleryEvent_page(id):
    GalleryEvents_imagesController.delete(id)
    GalleryEventsController.delete(id)
    return flask.redirect('/gallery')
@gallery_blueprint.route('/createGalleryEvent_page', methods=['GET']) 
@login_required
def createGalleryEvent_page():
    return flask.render_template(
            'gallery/createGallery_page.html'
        )
@gallery_blueprint.route('/createGalleryEvent_action', methods=['POST']) 
@login_required
def createGalleryEvent_action():
    if request.method == "POST":
        date = request.form.get('date')
        title = request.form.get('title')
        images = request.files.getlist('files') # множественная загрузка
    galleryEvent = GalleryEventsController.add(
        date=date,
        title=title
    )
    dir_name = current_app.appСontorller.make_categoryDir('galleryEvent')
    for file in images:
        filename = file.filename
        if Path(filename).suffix != '.webp':
            fileSrc = os.path.join(current_app.appСontorller.tempImg, filename)
            file.save(fileSrc) # сохраняем файл во временную папку
            webp_src = ImagesController.convertImage(fileSrc, dir_name=dir_name)
            filename = str(Path(filename).stem)+'.webp'
        else:
            webp_src = os.path.join(dir_name, filename) 
            file.save(webp_src)
        image = ImagesController.add(
            filename=filename,
            src=webp_src)
        GalleryEvents_imagesController.add(
            image_id=image.id,
            galleryEvent_id=galleryEvent.id
        )
    return flask.redirect('/gallery')
@gallery_blueprint.route('/updateGalleryEvent_page/<id>', methods=['GET']) 
@login_required
def updateGalleryEvent_page(id):
    return flask.render_template(
            'gallery/updateGalleryEvent_page.html',
            gallery = GalleryEvents_imagesController.get_cur_gallery(id)
        )
@gallery_blueprint.route('/updateImage_action/<GalleryEvents_images>', methods=['POST']) 
@login_required
def updateImage_action(GalleryEvents_images):
    GalleryEvents_imagesController.update(
        GalleryEvents_imagesController.show_gallery_images(galleryEvent_id=GalleryEvents_images[0]),
        galleryEvent_id=GalleryEvents_images[0],
        image_id=GalleryEvents_images[1]
    )
@gallery_blueprint.route('/updateGalleryEvent_action/<id>', methods=['POST']) 
@login_required
def updateGalleryEvent_action(id):
    if request.method == "POST":
        date = request.form.get('date')
        title = request.form.get('title')
        galleryEvent = GalleryEventsController.update(
            id,
            date=date,
            title=title
        )
    return flask.redirect('/gallery')
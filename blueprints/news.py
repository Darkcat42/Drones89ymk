# импорты системных библиотек
import flask, os, datetime
from flask_login import login_required
from flask import render_template, request, Blueprint, current_app
from Controllers.NewsController import NewsController
from Controllers.ImagesController import ImagesController
from pathlib import Path

news_blueprint = Blueprint('news_bluep', __name__) 
# маршруты для страницы новости
@news_blueprint.route('/news/')
def news():
    """переход на страницу c новостями"""
    news = NewsController.getNews()
    return render_template(
        'news/news.html',
        news=news,
        )
@news_blueprint.route('/news/more/<id>')
def current_news(id):
    """переход на страницу новости"""
    current_news = NewsController.getNew_dict(id)
    return render_template(
        'news/current_news.html',
        current_news=current_news,
        )
@news_blueprint.route('/news/create/<msg>', methods=['GET']) 
@login_required
def createNews_page(msg):
        return flask.render_template(
            'news/add_news.html',
            msg = msg
        )
@news_blueprint.route('/news/delete/<id>')
@login_required
def deleteNews_action(id):
    NewsController.delete(id)
    return flask.redirect('/news')
@news_blueprint.route('/news/create/submit', methods=['POST'])
@login_required
def addNews_action():
    if request.method == "POST":
        title = request.form.get('news_title')
        text = request.form.get('news_text')
        if title == '' and text == '':
            return flask.redirect('/actions_news/create/Заполните поля!')
     
        file = request.files['news_file']
        filename = file.filename
        if filename == '':
            return flask.redirect('/actions_news/create/Установите изображение!')
        dir_name = current_app.appСontorller.make_categoryDir('news')
        if Path(filename).suffix != '.webp':
            fileSrc = os.path.join(current_app.appСontorller.tempImg, filename)
            current_app.appСontorller.make_recurDirs(current_app.appСontorller.tempImg)
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
       
        NewsController.addNews(
            title=title,
            news_desc=text,
            date=datetime.datetime.today().strftime('%Y-%m-%d'),
            image_id=image_id,
        )
        return flask.redirect('/news')
@news_blueprint.route('/news/update/<msg>/<id>', methods=['GET', 'POST'])
@login_required
def updateNews_page(id, msg):
        return flask.render_template(
            'news/update_news.html',
            news = NewsController.getNew_dict(id),
            msg = msg
        )
@news_blueprint.route('/news/update/submit/<id>', methods=['POST'])
@login_required
def updateNews_action(id):
    cur_news = NewsController.getNew_dict(id)
    if request.method == "POST":
        title = request.form.get('news_title')
        text = request.form.get('news_text')
        date = request.form.get('news_date')
        if date == '':
            date=cur_news['date']
        file = request.files['news_file']
        if file.filename != "":
            try:
                filename = file.filename
                dir_name = current_app.appСontorller.make_categoryDir('news')
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
        else:
            image_id = cur_news['image_id']
        NewsController.update(
            id, 
            title=title,
            news_desc=text,
            date=date,
            image_id=image_id,
        )
        return flask.redirect('/news')
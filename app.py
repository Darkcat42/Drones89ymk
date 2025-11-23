# импорты пайтон и тп
import flask, flask_login
from flask_login import LoginManager, login_required, current_user, logout_user
from flask import Flask, render_template, request
from pathlib import Path
import datetime
from Controllers.NewsController import NewsController
# импорт контроллеров
from Controllers.UserController import UsersController
from Controllers.RoleController import RoleController
from Controllers.ScheduleController import ScheduleController
from Controllers.SectionsController import SectionsController
from Controllers.ImagesController import ImagesController
from Controllers.GalleryEventsController import GalleryEventsController
from Controllers.GalleryEvents_imagesController import GalleryEvents_imagesController 
"""создание и настройка приложения"""
app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.secret_key = 'jksdhf l;lkj&*~19273l;kaszdfop['
@login_manager.user_loader
def load_user(user_id): 
   """функция загрузки пользователя для flask_login"""
   return UsersController.show(int(user_id))
@login_manager.unauthorized_handler
def anon():
    """функция анонимного пользователя"""
    return flask.redirect('/')
@app.route('/favicon.ico') 
def fav_pass():
    """сброс ошибки переадресации на favicon.ico"""
    return 'favicon'
"""маршруты приложения"""
@app.route('/logout') 
def logout():
    """маршрут для выхода из авторизации"""
    logout_user()
    return flask.redirect('/')
@app.route('/') 
def index():
    """маршрут на главную"""
    return render_template(
        'index.html',
        scheduleDays=ScheduleController.get_ScheduleDays(),
        scheduleInfo=SectionsController.get_section_info('schedule'),
        edit_tools = False
        )
@app.route('/doc') 
def doc():
    """маршрут страницу документов"""
    return render_template('doc.html')
# @app.route('/policy') 
# def policy():
#     """маршрут policy.html"""
#     return render_template('policy.html')
@app.route('/build') 
def build():
    """маршрут на страницу сборок с дронами"""
    return render_template('build.html')

def open_file(src):
    with open(src, 'r') as html:
        return html.read()
@app.route('/loadModalBlock_anon/<blockName>')
def loadModalBlock_anon(blockName):
    """маршрут для загрузки модальных блоков неавторизоавнных пользователей"""
    match blockName:
        case 'login':
            return open_file('templates/html_modal_blocks/login.html')


@app.route('/loadModalBlock_user/<blockName>')
@login_required
def loadModalBlock_user(blockName):
    """маршрут для загрузки модальных блоков для пользователей прошедших авторизацию"""
    match blockName:
        case 'schedule':
            return open_file('templates/html_modal_blocks/schedule.html')
        case 'news_modal':
            return open_file('templates/html_modal_blocks/news_modal.html')
        case 'galleryEvent_modal':
            return open_file('templates/html_modal_blocks/galleryEvent_modal.html')
        
@app.route('/admin_panel')
@login_required
def admin_panel():
    return render_template(
        'admin_panel.html',
        scheduleDays=ScheduleController.get_ScheduleDays(),
        scheduleInfo=SectionsController.get_section_info('schedule'),
        edit_tools = True
        )
@app.route('/login', methods=['POST'])
def login(): 
    """маршрут для авторизации пользователя"""
    if request.method == "POST":
            login_form = request.form.get('login')
            user = UsersController.get_by_login(login_form)
            if login_form == user.login:
                passwd_form = request.form.get('password')
                if passwd_form == user.password:
                    flask_login.login_user(user)
                    role_name = RoleController.show(current_user.role_id).role_id
                    if role_name == 'administrator':
                        """маршрут на главную с функционалом администратора"""
                        return flask.redirect('/admin_panel')
                    elif role_name == 'editor':
                        """задел под роль редактора"""
                        pass
                    elif role_name == 'student':
                        """задел под роль студента"""
                        pass
                else:
                    return 'неверный логин или пароль'
    return flask.redirect('/')
# маршруты для блока расписания главной страницы
@app.route('/showScheduleDay/<id>', methods=['GET'])
@login_required
def showScheduleDay(id):
    return ScheduleController.get_currentScheduleDay(id)
@app.route('/updateScheduleDay/<id>', methods=['POST'])
@login_required
def updateScheduleDay(id):
    day_id = id
    data = request.get_json()
    ScheduleController.update(
        day_id, 
        location=data['location'],
        day = data['day'],
        start = data['start'],
        end = data['end']
        )
    data = ScheduleController.get_currentScheduleDay(day_id)
    return data
@app.route('/createScheduleDay', methods=['POST'])
@login_required
def createScheduleDay():
    if request.method == "POST":
        data = request.get_json()
        location = data['location']
        day = data['day']
        start = data['start']
        end = data['end']
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
        return current_day
@app.route('/deleteScheduleDay/<id>', methods=['GET'])
@login_required
def deleteScheduleDay(id):
    ScheduleController.delete(id=id)
    if ScheduleController.show(id) == None:
        return id
# маршруты для страницы новости
@app.route('/news') 
def news():
    news_list = NewsController.getNews()
    return render_template('news.html', news=news_list, edit_tools=True)
@app.route('/createNews', methods=['POST'])
@login_required
def createNews():
    if request.method == "POST":
        title = request.form.get('title')
        text = request.form.get('text')
        file = request.files['file']
        filename = file.filename
        src = f'static/temp/img/{filename}'
        file.save(src)
        webp_src = ImagesController.convertImage(src)
        filename = str(Path(filename).stem)+'.webp'
        ImagesController.add(
            filename=filename,
            src=webp_src)
        image_id = ImagesController.show(filename)
        NewsController.addNews(
            title=title,
            news_desc=text,
            date=datetime.datetime.today().strftime('%Y-%m-%d'),
            image_id=image_id,
        )
        new = NewsController.showLast()
        image_src = ImagesController.show_id(new.image_id).src

        new_data = {
            'id': new.id,
            'day': new.title,
            'start': new.news_desc,
            'end': new.date,
            'image_src': image_src
        }
        return new_data
# маршруты для страницы галерея
@app.route('/gallery') 
def gallery():
    """маршрут на страницу с галереей"""
    return render_template(
        'gallery.html',
        list_of_gallerys = GalleryEvents_imagesController.get_all_gallerys()
        )

@app.route('/addGalleryEvent', methods=['POST']) 
def addGalleryEvent():
    if request.method == "POST":
        date = request.form.get('date')
        title = request.form.get('title')
        images = request.files.getlist('files') # множественная загрузка
    galleryEvent = GalleryEventsController.add(
        date=date,
        title=title
    )
    for file in images:
        filename = file.filename
        if Path(filename).suffix != '.webp':
            src = f'static/temp/img/{filename}'
            file.save(src)
            webp_src = ImagesController.convertImage(src)
            filename = str(Path(filename).stem)+'.webp'
        else:
            src = f'static/webp/{filename}'
            file.save(src)
            webp_src = src
        image = ImagesController.add(
            filename=filename,
            src=webp_src)
        GalleryEvents_imagesController.add(
            image_id=image.id,
            galleryEvent_id=galleryEvent.id
        )
    return GalleryEvents_imagesController.get_cur_gallery(galleryEvent)

if __name__ == '__main__':
    app.run(debug=True)
# импорты пайтон и тп
import pathlib

import flask, flask_login, os, datetime
from pathlib import Path
from flask_login import LoginManager, login_required, current_user, logout_user
from flask import Flask, render_template, request
# импорт контроллеров
from Controllers.NewsController import NewsController
from Controllers.UserController import UsersController
from Controllers.RoleController import RoleController
from Controllers.ScheduleController import ScheduleController
from Controllers.SectionsController import SectionsController
from Controllers.ImagesController import ImagesController
from Controllers.GalleryEventsController import GalleryEventsController
from Controllers.GalleryEvents_imagesController import GalleryEvents_imagesController
class App_contorller():
    """класс для сторонних функций и данных приложения"""
    def __init__(self):
        self.checkMake_oneDir('static/webp')
        self.checkMake_oneDir('static/temp')
        self.checkMake_oneDir('static/temp/img') 
        self._dir_tempImg = f'static/temp/img'
        self._dir_webpImg = f'static/webp' 
    @property
    def dir_tempImg(self):
        """геттер для директории временных картинок"""
        return self._dir_tempImg
    @dir_tempImg.setter
    def dir_tempImg(self, value):
        """сеттер"""
        self._dir_tempImg = value
    @property
    def dir_webpImg(self):
        """геттер для директории webp картинок"""
        return self._dir_webpImg
    @dir_webpImg.setter
    def dir_webpImg(self, value):
        """сеттер"""
        self._dir_webpImg = value
    @staticmethod
    def open_file(src):
        """читает файл и возвращает результат, упрощает общий вид кода"""
        with open(src, 'r') as html:
            return html.read()
    @staticmethod
    def checkMake_oneDir(src):
        """проверка директории, если таковой нет то создает ее"""
        if os.path.isdir(src) != True:
            os.mkdir(src)
        else:
            print(src, 'директория существует')
    @staticmethod
    def checkMake_recurDirs(src):
        """проверка директории, если таковой нет то создает ее"""
        if os.path.isdir(src) != True:
            os.makedirs(src)
        else:
            print(src, 'директория существует')
    @classmethod
    def mkdir_cat_dir(cls, cat_dir):
        save_path = pathlib.Path('static/webp')
        print(save_path)
        calendar_date = str(datetime.datetime.today().strftime('%Y-%m-%d').replace('-', '_'))
        # checkMake_dir = lambda in_path: print('mkdir false', os.path.isdir(in_path)) if os.path.isdir(in_path) else os.mkdir(in_path)
        # checkMakes_dirs = lambda in_path: print('mkdir false', os.path.isdir(in_path)) if os.path.isdir(in_path) else os.makedirs(in_path)

        save_path = os.path.join(save_path, calendar_date, cat_dir)
        print(save_path)
        cls.checkMake_recurDirs(save_path)

        cur_dir_name = cat_dir + str(len(os.listdir(save_path)))
        save_path = os.path.join(save_path, cur_dir_name)
        print(save_path)
        cls.checkMake_oneDir(save_path)

        return save_path

# создание и настройка приложения
app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.secret_key = 'jksdhf l;lkj&*~19273l;kaszdfop['
# функциональные маршруты приложения 
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
# авторизация в приложение
@app.route('/login_page', methods=['GET'])
def login_page():
    return flask.render_template(
        'login/login.html'
    )
@app.route('/login_action', methods=['POST'])
def login():
    """маршрут для авторизации пользователя"""
    if request.method == "POST":
            login_form = request.form.get('login')
            user = UsersController.get_by_login(login_form)
            if user != None:
                # проверка на длину 
                
                passwd_form = request.form.get('password')
                if passwd_form == user.password:
                    flask_login.login_user(user)
                    role_name = current_user.role_id.role
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
@app.route('/logout') 
def logout():
    """маршрут для выхода из авторизации"""
    logout_user()
    return flask.redirect('/')
@app.route('/') 
def index():
    """маршрут на главную"""
    return render_template(
        'main/index.html',
        scheduleDays=ScheduleController.get_ScheduleDays(),
        scheduleInfo=SectionsController.get_section_info('schedule'),
        lastNews=NewsController.getLast_dict(),
        edit_tools = False
        )
@app.route('/admin_panel')
@login_required
def admin_panel():
    return render_template(
        'main/admin_panel.html',
        scheduleDays=ScheduleController.get_ScheduleDays(),
        scheduleInfo=SectionsController.get_section_info('schedule'),
        lastNews=NewsController.getLast_dict(),
        edit_tools = True
        )

# маршруты для блока расписания главной страницы
@app.route('/updateSchedule_page/<id>', methods=['GET'])
@login_required
def updateSchedule_page(id):
        return flask.render_template(
            'schedule/updateSchedule_action.html',
            edit_schedule = True,
            day = ScheduleController.get_currentScheduleDay(id)
        )
@app.route('/updateSchedule_action/<id>', methods=['POST'])
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
@app.route('/createSchedule_page', methods=['GET'])
@login_required
def createSchedule_page():
        return flask.render_template(
            'schedule/createSchedule_action.html',
            edit_schedule = False,
            day = None
        )
@app.route('/createSchedule_action', methods=['POST'])
@login_required
def createScheduleDay():
    if request.method == "POST":
        location = request.form.get('location')
        day = request.form.get('day')
        start = request.form.get('start')
        end = request.form.get('end')
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
@app.route('/deleteScheduleDay/<id>', methods=['GET'])
@login_required
def deleteScheduleDay(id):
    result = ScheduleController.delete(id=id)
    return flask.redirect('/admin_panel#schedule')
# маршруты для страницы сборок
@app.route('/build')
def build():
    """маршрут на страницу сборок с дронами"""
    return render_template('build/build.html')
# маршруты для страницы документов с правилами
@app.route('/doc')
def doc():
    """маршрут страницу документов"""
    return render_template('doc.html')
# маршруты для страницы политики обработки персональных данных
@app.route('/policy')
def policy():
    """маршрут policy.html"""
    return render_template('policy.html')
# маршруты для страницы новости
@app.route('/updateNews_page/<id>', methods=['GET', 'POST'])
@login_required
def updateNews_page(id):
        return flask.render_template(
            'news/updateNews_action.html',
            news = NewsController.getNew_dict(id)
        )
@app.route('/updateNews_action/<id>', methods=['POST'])
@login_required
def updateNews_action(id):
    if request.method == "POST":
        title = request.form.get('news_title')
        text = request.form.get('news_text')
        try:
            file = request.files['news_file']
            filename = file.filename
            if Path(filename).suffix != '.webp':
                fileSrc = os.path.join(AppСontorller.dir_tempImg, filename)
                file.save(fileSrc) # сохраняем файл во временную папку
                dir_name = App_contorller.mkdir_cat_dir('news')
                webp_src = ImagesController.convertImage(fileSrc, dir_name) 
                filename = str(Path(filename).stem)+'.webp'
            else:
                webp_src = os.path.join(AppСontorller.dir_webpImg, filename) 
                file.save(webp_src)
            image = ImagesController.add(
                filename=filename,
                src=webp_src)
            image_id = image.id
        except:
            image_id = ImagesController.get()[0].id
        NewsController.update(
            id, 
            title=title,
            news_desc=text,
            date='доделать контроллер',
            image_id=image_id,
        )
        return flask.redirect('/news')
@app.route('/deleteNews_action/<id>')
@login_required
def deleteNews_action(id):
    NewsController.delete(id)
    return flask.redirect('/news')
@app.route('/news')
def news():
    edit_tools = False
    try:
        role_name = current_user.role_id.role
        if role_name == 'administrator':
            edit_tools = True
    except:
        pass
    news = NewsController.get()
    news_list = NewsController.getNews(news)
    return render_template(
        'news/news.html',
        news=news_list,
        edit_tools=edit_tools)
@app.route('/createNews_page', methods=['GET'])
@login_required
def createNews_page():
        return flask.render_template(
            'news/createNews_action.html',
            news = None
        )
@app.route('/createNews_action', methods=['POST'])
@login_required
def createNews_action():
    if request.method == "POST":
        title = request.form.get('news_title')
        text = request.form.get('news_text')
        try:
            file = request.files['news_file']
            filename = file.filename
            if Path(filename).suffix != '.webp':
                fileSrc = os.path.join(AppСontorller.dir_tempImg, filename)
                file.save(fileSrc) # сохраняем файл во временную папку
                dir_name = App_contorller.mkdir_cat_dir('news')
                webp_src = ImagesController.convertImage(fileSrc, dir_name) 
                filename = str(Path(filename).stem)+'.webp'
            else:
                webp_src = os.path.join(AppСontorller.dir_webpImg, filename) 
                file.save(webp_src)
            image = ImagesController.add(
                filename=filename,
                src=webp_src)
            image_id = image.id
        except:
            image_id = ImagesController.get()[0].id
        NewsController.addNews(
            title=title,
            news_desc=text,
            date=datetime.datetime.today().strftime('%Y-%m-%d'),
            image_id=image_id,
        )
        return flask.redirect('/news')
# маршруты для страницы галерея
@app.route('/gallery') 
def gallery():
    """маршрут на страницу с галереей"""
    edit_tools = False
    try:
        role_name = current_user.role_id.role
        if role_name == 'administrator':
            edit_tools = True
    except:
        pass
    return render_template(
        'gallery/gallery.html',
        list_of_gallerys = GalleryEvents_imagesController.get_all_gallerys(),
        edit_tools=edit_tools
        )
@app.route('/addGalleryEvent', methods=['POST']) 
@login_required
def addGalleryEvent():
    if request.method == "POST":
        date = request.form.get('date')
        title = request.form.get('title')
        images = request.files.getlist('files') # множественная загрузка
    galleryEvent = GalleryEventsController.add(
        date=date,
        title=title
    )
    dir_name = App_contorller.mkdir_cat_dir('galleryEvent')
    for file in images:
        filename = file.filename
        if Path(filename).suffix != '.webp':
            fileSrc = os.path.join(AppСontorller.dir_tempImg, filename)
            file.save(fileSrc) # сохраняем файл во временную папку
            webp_src = ImagesController.convertImage(fileSrc, dir_name=dir_name)
            filename = str(Path(filename).stem)+'.webp'
        else:
            webp_src = os.path.join(AppСontorller.dir_webpImg, filename) 
            file.save(webp_src)
        image = ImagesController.add(
            filename=filename,
            src=webp_src)
        GalleryEvents_imagesController.add(
            image_id=image.id,
            galleryEvent_id=galleryEvent.id
        )
    return GalleryEvents_imagesController.get_cur_gallery(galleryEvent)
if __name__ == '__main__':
    AppСontorller = App_contorller()
    app.run(debug=True)

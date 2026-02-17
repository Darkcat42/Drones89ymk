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
from Controllers.PersonsController import PersonsController
from Controllers.HardwaresController import HardwaresController
from Controllers.BuildController import BuildController
from Controllers.Builds_authorsController import Builds_authorsController
from Controllers.Builds_hardwaresController import Builds_hardwaresController
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
        with open(src, 'r') as file:
            return file.read()
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
# авторизация в приложении
@app.route('/login', methods=['GET']) 
def login_redirect():
    return flask.redirect(f'/login_page/{'login'}')
@app.route('/login_page/<msg>', methods=['GET'])
def login_page_msg(msg = ''):
    return flask.render_template(
        'login/login.html',
        msg = msg
    )
@app.route('/login_action', methods=['POST'])
def login():
    """маршрут для авторизации пользователя"""
    if request.method == "POST":
            login_form = request.form.get('login')
            passwd_form = request.form.get('password')
            if login_form == '' and passwd_form == '':
                return flask.redirect('/login_page/Заполните форму!') 
            else:
                user = UsersController.get_by_login(login_form)
                if user != None:
                    if passwd_form == user.password:
                        flask_login.login_user(user)
                        role_name = current_user.role_id.role
                        if role_name == 'administrator':
                            """маршрут на главную с функционалом администратора"""
                            return flask.redirect('/admin_panel')
                    else:
                        return flask.redirect(f'/login_page/неверный логин или пароль') 
    return flask.redirect(f'/login_page/неверный логин или пароль')
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
        lastNews=NewsController.getLast_dict()
        )
@app.route('/admin_panel')
@login_required
def admin_panel():
    return render_template(
        'main/admin_panel.html',
        scheduleDays=ScheduleController.get_ScheduleDays(),
        scheduleInfo=SectionsController.get_section_info('schedule'),
        lastNews=NewsController.getLast_dict()
        )
# маршруты для блока расписания главной страницы
@app.route('/updateSchedule_page/<id>', methods=['GET'])
@login_required
def updateSchedule_page(id):
        return flask.render_template(
            'schedule/updateSchedule_action.html',
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
@app.route('/actions_news/delete/<id>')
@login_required
def deleteNews_action(id):
    NewsController.delete(id)
    return flask.redirect('/news')
@app.route('/news')
def news():
    news = NewsController.get()
    news_list = NewsController.getNews(news)
    return render_template(
        'news/news.html',
        news=news_list,
        )
@app.route('/actions_news/<action>', methods=['GET'])
@login_required
def action_news(action):
    return flask.redirect(f'/actions_news/{action}')
@app.route('/actions_news/create/<msg>', methods=['GET'])
@login_required
def createNews_page(msg):
        return flask.render_template(
            'news/add_news.html',
            msg = msg
        )
@app.route('/actions_news/create/submit', methods=['POST'])
@login_required
def addNews_action():
    if request.method == "POST":
        title = request.form.get('news_title')
        text = request.form.get('news_text')
        if title == '' and text == '':
            return flask.redirect('/actions_news/create/Заполните поля!')
        try:
            file = request.files['news_file']
            filename = file.filename
            if filename == '':
                return flask.redirect('/actions_news/create/Установите изображение!')
            dir_name = App_contorller.mkdir_cat_dir('news')
            if Path(filename).suffix != '.webp':
                fileSrc = os.path.join(AppСontorller.dir_tempImg, filename)
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
        NewsController.addNews(
            title=title,
            news_desc=text,
            date=datetime.datetime.today().strftime('%Y-%m-%d'),
            image_id=image_id,
        )
        return flask.redirect('/news')
@app.route('/actions_news/update/<msg>/<id>', methods=['GET', 'POST'])
@login_required
def updateNews_page(id, msg):
        return flask.render_template(
            'news/update_news.html',
            news = NewsController.getNew_dict(id),
            msg = msg
        )
@app.route('/actions_news/update/submit/<id>', methods=['POST'])
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
                dir_name = App_contorller.mkdir_cat_dir('news')
                if Path(filename).suffix != '.webp':
                    fileSrc = os.path.join(AppСontorller.dir_tempImg, filename)
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
# маршруты для страницы галерея
@app.route('/gallery') 
def gallery():
    """маршрут на страницу с галереей"""
    return render_template(
        'gallery/gallery.html',
        list_of_gallerys = GalleryEvents_imagesController.get_all_gallerys()
        )
@app.route('/deleteGalleryEvent_page/<id>', methods=['GET']) 
@login_required
def deleteGalleryEvent_page(id):
    GalleryEvents_imagesController.delete(id)
    GalleryEventsController.delete(id)
    return flask.redirect('/gallery')
@app.route('/createGalleryEvent_page', methods=['GET']) 
@login_required
def createGalleryEvent_page():
    return flask.render_template(
            'gallery/createGallery_page.html'
        )
@app.route('/createGalleryEvent_action', methods=['POST']) 
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
    dir_name = App_contorller.mkdir_cat_dir('galleryEvent')
    for file in images:
        filename = file.filename
        if Path(filename).suffix != '.webp':
            fileSrc = os.path.join(AppСontorller.dir_tempImg, filename)
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
@app.route('/updateGalleryEvent_page/<id>', methods=['GET']) 
@login_required
def updateGalleryEvent_page(id):
    return flask.render_template(
            'gallery/updateGalleryEvent_page.html',
            gallery = GalleryEvents_imagesController.get_cur_gallery(id)
        )
@app.route('/updateImage_action/<GalleryEvents_images>', methods=['POST']) 
@login_required
def updateImage_action(GalleryEvents_images):
    GalleryEvents_imagesController.update(
        GalleryEvents_imagesController.show_gallery_images(galleryEvent_id=GalleryEvents_images[0]),
        galleryEvent_id=GalleryEvents_images[0],
        image_id=GalleryEvents_images[1]
    )
@app.route('/updateGalleryEvent_action/<id>', methods=['POST']) 
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
# маршруты для страницы персон
@app.route('/persons')
def persons():
    """маршрут на страницу """
    return render_template(
        'persons/persons.html',
        persons = PersonsController.getPersons()
        )
@app.route('/createPersons_page', methods=['GET']) 
@login_required
def createPerson_page():
    return flask.render_template(
        'persons/createPersons_page.html'
        )
@app.route('/createPersons_action', methods=['POST']) 
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
        dir_name = App_contorller.mkdir_cat_dir('persons')
        if Path(filename).suffix != '.webp':
            fileSrc = os.path.join(AppСontorller.dir_tempImg, filename)
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

@app.route('/updatePerson_action/<id>', methods=['POST']) 
@login_required
def updatePersons_action(id):
    if request.method == "POST":
        file = request.files.getlist('file') # множественная загрузка
        try:
            file = request.files.getlist('file') # множественная загрузка
            filename = file.filename
            dir_name = App_contorller.mkdir_cat_dir('persons')
            if Path(filename).suffix != '.webp':
                fileSrc = os.path.join(AppСontorller.dir_tempImg, filename)
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
@app.route('/updatePersons_page/<id>', methods=['GET']) 
@login_required
def updatePerson_page(id):
    return flask.render_template(
        'persons/updatePersons_page.html',
        person = PersonsController.get_cur_Person(id)
        )
@app.route('/deletePersons_action/<id>', methods=['GET']) 
@login_required
def deletePersons_action(id):
    PersonsController.delete(id)
    return flask.redirect('/persons')
# маршруты для страницы оборудования
@app.route('/hardwares')
@login_required
def hardwares():
    """маршрут на страницу """
    return render_template(
        'hardwares/hardwares.html',
        hardwares = HardwaresController.get_hardwares()
        )
@app.route('/createHardwares_page', methods=['GET']) 
@login_required
def createHardwares_page():
    return flask.render_template(
        'hardwares/createHardwares_page.html',
       
        )
@app.route('/createHardwares_action', methods=['POST']) 
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
@app.route('/updateHardwares_action/<id>', methods=['POST']) 
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
@app.route('/updateHardwares_page/<id>', methods=['GET']) 
@login_required
def updateHardwares_page(id):
    return flask.render_template(
        'hardwares/updateHardwares_page.html',
        hardware = HardwaresController.get_cur_hardware(id)
        )
@app.route('/deleteHardwares_action/<id>', methods=['GET']) 
@login_required
def deleteHardwares_action(id):
    HardwaresController.delete(id)
    return flask.redirect('/hardwares')
# маршруты для страницы сборок
@app.route('/build')
def build():
    """маршрут на страницу сборок с дронами"""
    return render_template(
        'builds/build.html',
        builds = BuildController.getBuilds()
        )
@app.route('/createBuilds_page', methods=['GET']) 
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
@app.route('/createBuilds_action', methods=['POST']) 
@login_required
def createBuilds_action():
    if request.method == "POST":
        file = request.files['file'] 
        try:
            filename = file.filename
            dir_name = App_contorller.mkdir_cat_dir('builds')
            if Path(filename).suffix != '.webp':
                fileSrc = os.path.join(AppСontorller.dir_tempImg, filename)
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
@app.route('/updateBuilds_action/<id>', methods=['POST']) 
@login_required
def updateBuilds_action(id):
    if request.method == "POST":
        file = request.files['file']
        # file = request.files('file') 
        try:
            # file = request.files.getlist('file') # множественная загрузка
            filename = file.filename
            dir_name = App_contorller.mkdir_cat_dir('builds')
            if Path(filename).suffix != '.webp':
                fileSrc = os.path.join(AppСontorller.dir_tempImg, filename)
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
@app.route('/updateBuilds_page/<id>', methods=['GET']) 
@login_required
def updateBuilds_page(id):
    return flask.render_template(
        'builds/updateBuilds_page.html',
        hardware = HardwaresController.get_cur_hardware(id)
        )
@app.route('/deleteBuilds_action/<id>', methods=['GET']) 
@login_required
def deleteBuilds_action(id):
    BuildController.delete(id)
    return flask.redirect('/build')

if __name__ == '__main__':
    AppСontorller = App_contorller()
    app.run(debug=True)

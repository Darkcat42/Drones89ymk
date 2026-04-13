# импорты системных библиотек
from flask_login import LoginManager
from flask_admin import Admin
from flask import Flask, request, render_template, flash
from flask import redirect as flask_redirect
from dotenv import set_key
from Models.Base import Base
import os
# импорт классов приложения
from connection.connect import init_db, reload_db, db_is_ready
from Controllers.UserController import UsersController
# from main import App_contorller
def create_flaskApp():
    init_db_status = init_db() # Инициализация БД
    print(init_db_status)
    # создание и настройка приложения flask
    app = Flask(__name__) 
    flask_admin = Admin(app, name='Панель администратора')
    login_manager = LoginManager()
    login_manager.init_app(app)
    # Регистрируем модели админки ОДИН РАЗ при старте
    from main import App_controller  # осторожно с циклическими импортами
    models_with_views = App_controller.models_importer()
    flask_admin.add_views(*models_with_views)
    # функциональные маршруты приложения 
    @app.context_processor
    def db_is_ready_context():
        global db_is_ready
        return {'init_db_status' : init_db_status}

    @login_manager.user_loader
    def load_user(user_id): 
        # функция загрузки пользователя для flask_login
        if not init_db_status:
            return None  # Без БД пользователей нет
        try:
            return UsersController.show_id(int(user_id))
        except:
            return None
        # return UsersController.show_id(int(user_id))
    @login_manager.unauthorized_handler
    def anon():
        # функция анонимного пользователя 
        return flask_redirect('/')
    @app.route('/favicon.ico') 
    def fav_pass():
        """сброс ошибки переадресации на favicon.ico"""
        return 'favicon'
    @app.route('/connect_sql', methods=['GET', 'POST']) 
    def connect_sql():
        if request.method == 'POST':
            # загружаем данные из формы
            name = request.form.get('name')
            login = request.form.get('login')
            passwd = request.form.get('passwd')
            ip = request.form.get('ip')
            port = request.form.get('port')
            root = os.path.dirname(__file__)
            env_path = os.path.join(root, 'static', 'config', 'db.env')
            set_key(env_path, 'name', name)
            set_key(env_path, 'login', login)
            set_key(env_path, 'passwd', passwd)
            set_key(env_path, 'ip', ip)
            set_key(env_path, 'port', port)
            # Переподключаем БД (без перерегистрации админки)
            if reload_db():
                # Создаём все таблицы после успешного подключения
                Base.ensure_tables()
                flash('Подключение к базе данных выполнено успешно!')
            else:
                flash('Не удалось подключиться к базе данных.', 'error')
        return flask_redirect('/admin/?tab_page=base')
    @app.route('/add_sql', methods=['GET', 'POST']) 
    def add_sql():
        return render_template('index/connect.html')
    # запоминаем наши модули
    app.config['flask_admin'] = flask_admin
    app.config['login_manager'] = login_manager
    app.config['init_db_status'] = init_db_status
    return app






# импорты системных библиотек
from flask_login import LoginManager
from flask_admin import Admin
from flask_babel import Babel
from flask import Flask
from flask import redirect as flask_redirect
# импорт классов приложения
from Controllers.UserController import UsersController
from main import App_contorller

# создание и настройка приложения
"""
логика маршрутизации:
    прим. /news/update/<msg>/<id> где 
        /раздел/действие/сообщение/номерОбъекта
"""
# настройка flask
app = Flask(__name__) 
# определения языка приложения
def get_locale():
    return 'ru'
babel = Babel(app, locale_selector=get_locale) # аргумент требует функцию
app.appСontorller = App_contorller() # добавляем свой класс с данными в приложение
# регистрация блюпринтов
app.appСontorller.registerAll_blueprints(app)
# настройка flask_admin
flask_admin = Admin(app, name='Панель администратора')
flask_admin.base_template ='flask_admin/master.html'
modelsWithView = app.appСontorller.models_importer()
flask_admin.add_views(*modelsWithView)
# настройка flask_login
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
    return flask_redirect('/')
@app.route('/favicon.ico') 
def fav_pass():
    """сброс ошибки переадресации на favicon.ico"""
    return 'favicon'
if __name__ == '__main__':
    app.run(debug=True)



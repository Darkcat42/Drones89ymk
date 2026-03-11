# импорты системных библиотек
from flask_login import LoginManager
from flask import Flask
from flask import redirect as flask_redirect
# импорт классов приложения
from Controllers.UserController import UsersController
from main import App_contorller
# импортирование блюпринтов
from blueprints.builds import builds_blueprint
from blueprints.gallary import gallery_blueprint
from blueprints.hardwares import hardwares_blueprint
from blueprints.index import index_blueprint
from blueprints.login import login_blueprint
from blueprints.news import news_blueprint
from blueprints.persons import persons_blueprint
from blueprints.schedule import schedule_blueprint
# создание и настройка приложения
"""
логика маршрутизации:
    прим. /news/update/<msg>/<id> где 
        /раздел/действие/сообщение/номерОбъекта
"""
# настройка flask
app = Flask(__name__) 
app.appСontorller = App_contorller() # добавляем свой класс с данными в приложение
# регистрация блюпринтов
app.register_blueprint(builds_blueprint)
app.register_blueprint(gallery_blueprint)
app.register_blueprint(hardwares_blueprint)
app.register_blueprint(index_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(news_blueprint)
app.register_blueprint(persons_blueprint)
app.register_blueprint(schedule_blueprint)
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



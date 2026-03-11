# импорты системных библиотек
import flask, os, datetime, flask_login
from flask_login import login_required, logout_user, current_user
from flask import render_template, request, Blueprint, current_app
from Controllers.UserController import UsersController


login_blueprint = Blueprint('login_bluep', __name__)
# авторизация в приложении
@login_blueprint.route('/login', methods=['GET']) 
def login_redirect():
    return flask.redirect('/login_page/login')
@login_blueprint.route('/login_page/<msg>', methods=['GET'])
def login_page_msg(msg = ''):
    return flask.render_template(
        'login/login.html',
        msg = msg)
@login_blueprint.route('/login_action', methods=['POST'])
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
@login_blueprint.route('/logout') 
def logout():
    """маршрут для выхода из авторизации"""
    logout_user()
    return flask.redirect('/')
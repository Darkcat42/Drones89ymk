import flask
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from flask import Flask, render_template, request, url_for, redirect
import flask_login
from Controllers.UserController import UsersController
from Controllers.RoleController import RoleController
from Controllers.WebpageController import WebpageController
from Controllers.MainBlockController import MainblockController 

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.secret_key = 'jksdhf l;lkj&*~19273l;kaszdfop['
@login_manager.user_loader
def load_user(user_id): # загрузка пользователя
   return UsersController.show(int(user_id))
@login_manager.unauthorized_handler
def anon():
    return flask.redirect('/')
@app.route('/') # МАРШРУТ редирект на главную
def main():
    return redirect('/main')
@app.route('/favicon.ico') # МАРШРУТ редирект на главную
def fav_pass():
    return 'favicon'

@app.route('/<webpage>') # МАРШРУТ на страницу
def index(webpage):
    webpage = str('/')+webpage
    webpage = WebpageController.get_by_url(webpage)
    mainblocks = MainblockController.get_blocks_where_webpage(int(webpage.id))
    mainblocks_list = MainblockController.get_order_by_mainblocks(mainblocks)
    print(mainblocks_list)
    print(mainblocks_list)
    print(mainblocks_list)
    print(mainblocks_list)
    print(mainblocks_list)
    webpage_links = WebpageController.get_order_by_webpages()
    webpage_name = webpage.name
    webpage_url = webpage.url
    if current_user.is_authenticated == True:
        return redirect(f'/edit/{webpage_url}')
    return render_template(
        'index.html', 
        links=webpage_links, 
        webpage_name=webpage_name,
        webpage_url=webpage_url,
        mainblocks_list=mainblocks_list
        )

@app.route('/edit/<webpage>') # МАРШРУТ на главную
@login_required
def edit(webpage):
    role_name = RoleController.show(current_user.role).role
    webpage = str('/')+webpage
    webpage = WebpageController.get_by_url(webpage)
    mainblocks = MainblockController.get_blocks_where_webpage(int(webpage.id))
    mainblocks_list = MainblockController.get_order_by_mainblocks(mainblocks)
    webpage_links = WebpageController.get_order_by_webpages()
    webpage_name = webpage.name
    webpage_url = webpage.url
    return render_template(
        'index.html', 
        links=webpage_links, 
        role=role_name, 
        webpage_name=webpage_name,
        webpage_url=webpage_url,
        mainblocks_list=mainblocks_list)
        # mainblocks_list.append(mainblocks_obj.html_id)
        # mainblocks_list.append(mainblocks_obj.title_id)
        # mainblocks_list.append(mainblocks_obj.paragraph_id)
        # mainblocks_list.append(mainblocks_obj.media_id)
        # mainblocks_list.append(mainblocks_obj.position)
@app.route('/logout') # МАРШРУТ для выхода из аккаунта
def logout():
    logout_user()
    return flask.redirect('/main')
@app.route('/autorization', methods=['POST']) # МАРШРУТ функция авторизации
def autorization():
    if request.method == "POST":
        login = request.form.get('login')
        passwd = request.form.get('password')
        if UsersController.get_by_login(login) != None or '':
            user = UsersController.get_by_login(login)
            if user.password == passwd:
                flask_login.login_user(user)
                role_name = RoleController.show(current_user.role).role
                if role_name == 'administrator':
                    return flask.redirect('/edit/main')
                else:
                    flask.redirect('/')
    return 'неправильный пароль или логин'

@app.route('/load_modal_form_login') # модальное окно для авторизации
def load_modal_form_login():
    modal_form_login = """<div class="container">
    <div class="card_right row fix-mar">
    <form class="modal_form_login" action="/autorization" method="post">
    <input id="login" type="text" name="login" placeholder="Введите логин">
    <input id="password" type="text" name="password" placeholder="Введите пароль">
    <input type="submit" value="Вход">
    </form>
    </div>
    </div>"""
    return modal_form_login

@app.route('/load_modal_menu_edit') # модальное окно для редактирования ссылок меню
def load_modal_menu_edit():
    modal_menu_edit = """

"""
    return modal_menu_edit

@login_required
@app.route('/delete_link/<int:id>', methods=['POST', "GET"]) # МАРШРУТ функцтя добавления шаблона в БД
def delete_link(id):
    WebpageController.delete(id)
    return redirect('/')
@app.route('/popap_add_web_page', methods=['POST', 'GET']) # МАРШРУТ на главную
@login_required
def popap_add_web_page():
    url = flask.request.form.get('url')
    name = flask.request.form.get('name')
    webpage_url = flask.request.form.get('webpage_url')
    type_link = flask.request.form.get('type_link')
    position = WebpageController.get_links_order_by_pos()[-1].position
    if url[0] != '#':
        url = '/'+str(url)
    WebpageController.add_link(
        name=name,
        url=url,
        type_link=type_link,
        position=int(position)+1
    )
    return redirect(f'/edit/{webpage_url}')
@app.route('/popap_edit_web_page/', methods=['POST', 'GET']) # МАРШРУТ на главную
@login_required
def popap_edit_web_page():
    data_from_url = flask.request.args.get('query', default=0, type=str)
    data = data_from_url.split(', ')
    url = str(data[0])
    name = str(data[1])
    str_data = f'{url}, {name}' 
    return str_data























if __name__ == '__main__':
    app.run(debug=True) 
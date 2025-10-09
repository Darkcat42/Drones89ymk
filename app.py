import flask, flask_login
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from flask import Flask, render_template, request, url_for, redirect 
from Controllers.UserController import UsersController
from Controllers.RoleController import RoleController
from Controllers.WebpageController import WebpageController
from Controllers.MainBlockController import MainblockController 
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
@app.route('/') 
def main():
    """функция переадресации на главную"""
    return redirect('/main')
@app.route('/favicon.ico') 
def fav_pass():
    """сброс ошибки переадресации на favicon.ico"""
    return 'favicon'
@app.route('/<webpage>') 
def index(webpage):
    """маршрут для гостей на веб-страницы сайта"""
    webpage = str('/')+webpage
    webpage = WebpageController.get_by_url(webpage)
    mainblocks = MainblockController.get_blocks_where_webpage(int(webpage.id))
    mainblocks_list = MainblockController.get_order_by_mainblocks(mainblocks)
    # print(mainblocks_list)
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
        mainblocks_list=mainblocks_list,
        mainblocks=mainblocks
    )
@app.route('/edit/<webpage>') 
@login_required
def edit(webpage):
    """маршрут для авторизованных пользователей на веб-страницы сайта"""
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
@app.route('/logout') 
def logout():
    """маршрут для выхода из авторизации"""
    logout_user()
    return flask.redirect('/main')
@app.route('/autorization', methods=['POST']) 
def autorization():
    """маршрут для авторизации из формы"""
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
@app.route('/load_modal_form_login') 
def load_modal_form_login():
    """маршрут для загрузки формы авторизации"""
    modal_form_login = """
    <div class="container">
        <div class="card_right row fix-mar">
            <form class="modal_form_login" action="/autorization" method="post">
                <input id="login" type="text" name="login" placeholder="Введите логин">
                <input id="password" type="text" name="password" placeholder="Введите пароль">
                <input class="modal_submit" type="submit" value="Вход">
            </form>
        </div>
    </div>"""
    return modal_form_login
@app.route('/load_modal_menu_edit') 
def load_modal_menu_edit():
    """маршрут для загрузки формы редактирования ссылок главного меню"""
    modal_menu_edit = """
<form action="/add_menu_link"> 
                <p>выберите тип ссылки:</p>
                <select name="select_type" >
                    <option data-id="1">новая веб-страница</option>
                    <option name="edit_menu_type">новый якорь</option>
                    <option name="edit_menu_type">страница сайта</option>
                </select>
                <p>выберите маршрут:</p>
                <select name="menu_edit_content" > 
                    <option>веб-страница будет в цикле из бд</option>
                </select>
                <select name="menu_edit_content" class="My_D_none"> 
                    <option>якори будут в цикле из бд</option>
                </select>
                    <input  name="" type="text" placeholder="введите название ссылки">
                    <input  name="" type="text" placeholder="введите url ссылки">
                    <input  class="modal_submit" name="" type="submit" value="Создать">
            </form>
"""
    return modal_menu_edit
@app.route('/delete_menu_link/<int:id>', methods=['POST', "GET"])
def delete_link(id):
    WebpageController.delete(id)
    return redirect('/')
@app.route('/add_menu_link', methods=['POST', 'GET'])
@login_required
def add_web_page():
# переработать только для ссылок, добавить проверку на повтор или недопуск
    url = flask.request.form.get('url')
    webpage_url = flask.request.form.get('webpage_url')
    type_link = flask.request.form.get('type_link')
    position = WebpageController.get_links_order_by_pos()[-1].position
    if url[0] != '#':
        url = '/'+str(url)
    WebpageController.add_link(
        url=url,
        type_link=type_link,
        position=int(position)+1
    )
    return redirect(f'/edit/{webpage_url}')
# коммит тест
# @app.route('/new_mainblock')
# def load_modal_form_login():
#     pass
# @app.route('/empty_mainblock')
# def load_modal_form_login():
#     pass
# маршруты для работы с веб страницами - переработать
# @login_required

# @app.route('/popap_edit_web_page/', methods=['POST', 'GET']) # МАРШРУТ на главную
# @login_required
# def popap_edit_web_page():
#     data_from_url = flask.request.args.get('query', default=0, type=str)
#     data = data_from_url.split(', ')
#     url = str(data[0])
#     name = str(data[1])
#     str_data = f'{url}, {name}' 
#     return str_data























if __name__ == '__main__':
    app.run(debug=True) 
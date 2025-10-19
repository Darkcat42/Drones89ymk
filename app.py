# импорты пайтон и тп
import flask, flask_login
from flask_login import LoginManager, login_required, current_user, logout_user
from flask import Flask, render_template, request
# импорт контроллеров
from Controllers.UserController import UsersController
from Controllers.RoleController import RoleController
from Controllers.TableController import Time_tableController

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
        table_rows=Time_tableController.get_table_rows()
        )
@app.route('/doc') 
def doc():
    """маршрут страницу документов"""
    return render_template('doc.html')
@app.route('/gallery') 
def gallery():
    """маршрут на страницу с галереей"""
    return render_template('gallery.html')
# @app.route('/policy') 
# def policy():
#     """маршрут policy.html"""
#     return render_template('policy.html')
@app.route('/build') 
def build():
    """маршрут на страницу сборок с дронами"""
    return render_template('build.html')
@app.route('/load_modal_form_login')
def load_modal_form_login():
    """маршрут для загрузки формы авторизации"""
    with open('templates/modal_login.html', 'r') as html:
        modal_form_login = html.read()
        html.close()
    return modal_form_login
@app.route('/login', methods=['POST'])
def login(): 
    """маршрут для авторизации пользователя"""
    if request.method == "POST":
        # try:
            login_form = request.form.get('login')
            user = UsersController.get_by_login(login_form)
            if login_form == user.login:
                passwd_form = request.form.get('password')
                if passwd_form == user.password:
                    flask_login.login_user(user)
                    role_name = RoleController.show(current_user.role).role
                    if role_name == 'administrator':
                        """маршрут на главную с функционалом администратора"""
                        return render_template(
                            'admin_index.html', 
                            table_rows=Time_tableController.get_table_rows()
                            )
                    elif role_name == 'editor':
                        """задел под роль редактора и тп"""
                        pass
                else:
                    return 'неверный логин или пароль'
        # except:
        #     print('ошибка')
    return flask.redirect('/')

@app.route('/admin_index')
@login_required
def admin_index():
    return render_template('admin_index.html', role='role_name')















if __name__ == '__main__':
    app.run(debug=True) 
# @app.route('/<webpage>')
# def index(webpage):
#     """маршрут для гостей на веб-страницы сайта"""
#     webpage = str('/')+webpage
#     webpage = WebpageController.get_by_url(webpage)
#     mainblocks = MainblockController.get_blocks_where_webpage(int(webpage.id))
#     mainblocks_list = MainblockController.get_order_by_mainblocks(mainblocks)
#     # print(mainblocks_list)
#     webpage_links = WebpageController.get_order_by_webpages()
#     webpage_name = webpage.name
#     webpage_url = webpage.url
#     if current_user.is_authenticated == True:
#         return redirect(f'/edit/{webpage_url}')
#     return render_template(
#         'index.html',
#         links=webpage_links,
#         webpage_name=webpage_name,
#         webpage_url=webpage_url,
#         mainblocks_list=mainblocks_list,
#         mainblocks=mainblocks
#     )
# @app.route('/edit/<webpage>')
# @login_required
# def edit(webpage):
#     """маршрут для авторизованных пользователей на веб-страницы сайта"""
#     role_name = RoleController.show(current_user.role).role
#     webpage = str('/')+webpage
#     webpage = WebpageController.get_by_url(webpage)
#     mainblocks = MainblockController.get_blocks_where_webpage(int(webpage.id))
#     mainblocks_list = MainblockController.get_order_by_mainblocks(mainblocks)
#     webpage_links = WebpageController.get_order_by_webpages()
#     webpage_name = webpage.name
#     webpage_url = webpage.url
#     return render_template(
#         'index.html',
#         links=webpage_links,
#         role=role_name,
#         webpage_name=webpage_name,
#         webpage_url=webpage_url,
#         mainblocks_list=mainblocks_list)
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
# @app.route('/load_modal_menu_edit')
# def load_modal_menu_edit():
#     """маршрут для загрузки формы редактирования ссылок главного меню"""
#     modal_menu_edit = """
# <form action="/add_menu_link"> 
#                     <select name="select_type" >
#                         <option data-id="1">выберите тип ссылки:</option>
#                         <option data-id="1">новая веб-страница</option>
#                         <option name="edit_menu_type">новый якорь</option>
#                         <option name="edit_menu_type">страница сайта</option>
#                     </select>
#                     <select name="menu_edit_content" > 
#                         <option>выберите маршрут:</option>
#                         <option>веб-страница будет в цикле из бд</option>
#                     </select>
#                     <select name="menu_edit_content" class="My_D_none"> 
#                         <option>якори будут в цикле из бд</option>
#                     </select>
#                     <input  name="" type="text" placeholder="введите название ссылки">
#                     <input  name="" type="text" placeholder="введите url ссылки">
#                     <input  class="modal_submit" name="" type="submit" value="Создать">
#             </form>
# """
#     return modal_menu_edit

# @app.route('/delete_menu_link/<int:id>', methods=['POST', "GET"])
# @login_required
# def delete_link(id):
#     print('delete link')
#     return 'link was deleted'
# @app.route('/add_menu_link', methods=['POST', 'GET'])
# @login_required
# def add_web_page():
# # переработать только для ссылок, добавить проверку на повтор или недопуск
#     url = flask.request.form.get('url')
#     webpage_url = flask.request.form.get('webpage_url')
#     type_link = flask.request.form.get('type_link')
#     if url[0] != '#':
#         url = '/'+str(url)
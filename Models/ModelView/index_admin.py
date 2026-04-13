# импорты
from flask_admin import Admin, AdminIndexView, expose
class index_admin(AdminIndexView):
    template = 'admin/index.html'
    uses_upload = True
        
    # @expose
    # def index(self):
    # для template

    
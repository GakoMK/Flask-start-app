from flask_admin import Admin, AdminIndexView, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink
from app import app, db, login_manager
from flask import url_for, redirect, render_template
from flask_login import current_user
from models import User

# # LOGIN
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class MyModelView(ModelView):
    # https://flask-admin.readthedocs.io/en/latest/introduction/
    # CRUD operations
    can_delete = False  # disable model deletion
    # can_create = False
    # can_edit = False
    can_view_details = True  
    # Removing columns
    column_exclude_list = ['password_hash', ]
    # Make columns searchable
    column_searchable_list = ['email']
    # column_filters = ['email']
    # column_editable_list = ['email'] #inline editing
    # modal window
    create_modal = True
    edit_modal = True
    # remove fields from the create and edit forms:
    form_excluded_columns = ['active']
    can_export = True

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login'))

class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login'))

class CustomView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/analytics_index.html')



# ADMIN
# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'simplex'
admin = Admin(app, index_view=MyAdminIndexView(name='NOT HOME'), template_mode='bootstrap4')
admin.add_view(MyModelView(User, db.session, category='Database table'))

admin.add_view(MyAdminIndexView(name='Hello 1', endpoint='test1', category='Test'))
admin.add_view(MyAdminIndexView(name='Hello 2', endpoint='test2', category='Test'))
admin.add_view(MyAdminIndexView(name='Hello 3', endpoint='test3', category='Test'))

admin.add_link(MenuLink(name='Home Page', url='/', endpoint='Homepage'))

admin.add_view(CustomView(name='Analytics', endpoint='analytics'))
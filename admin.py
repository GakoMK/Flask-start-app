from flask_admin import Admin, AdminIndexView, helpers, expose
from flask_admin.contrib.sqla import ModelView
from werkzeug.security import generate_password_hash
from app import app, db, login_manager
from flask import url_for, redirect, render_template, request
from flask_login import current_user, logout_user, login_user
from models import User

# # LOGIN
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login'))

class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login'))

# ADMIN
# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'simplex'
admin = Admin(app, index_view=MyAdminIndexView(), template_mode='bootstrap4')
admin.add_view(MyModelView(User, db.session))
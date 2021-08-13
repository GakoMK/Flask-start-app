import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdashdfljahsdf293y4q'
# db location
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "data\\app.db"))

# app
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config['SECRET_KEY'] = "p9Bv<3Eid9%$i01"
bcrypt = Bcrypt(app)
Bootstrap(app)
db = SQLAlchemy(app)

#1 book
login_manager = LoginManager(app)
login_manager.login_view = 'login'



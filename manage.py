import os
from flask import Flask
import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand, migrate
    
    
app = Flask(__name__)
# db
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "data\\app.db"))

# app
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config['SECRET_KEY'] = "p9Bv<3Eid9%$i01"

db = SQLAlchemy(app)

# migrate
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(255))
    name = db.Column(db.String(64))
    slug = db.Column(db.String(64), unique=True)
    active = db.Column(db.Boolean, default=True)
    created_timestamp = db.Column(db.DateTime, default=datetime.datetime.now)



if __name__ == '__main__':
    manager.run()




# @ INSTRUKCJA
    #pip install -r requirements.txt

    #python app.py db init
    #python app.py db migrate
    #python app.py db upgrade
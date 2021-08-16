from app import db, bcrypt
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(255))
    active = db.Column(db.Boolean, default=True)

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    # Flask-Login interface..
    # def get_id(self):
    #     return str(self.id)

    # def is_authenticated(self):
    #     return True

    # def is_active(self):
    #     return self.active

    # def is_anonymous(self):
    #     return False

    # def __repr__(self):
    #     return '<id {}/{}>'.format(self.id, self.username)  


    @staticmethod
    def make_password(plaintext):
        return bcrypt.generate_password_hash(plaintext)

    def check_password(self, raw_password):
        return bcrypt.check_password_hash(self.password_hash, raw_password)


    @classmethod
    def create(cls, email, password, **kwargs):
        return User( 
            email=email, 
            password_hash=User.make_password(password),
            **kwargs
            )


    @staticmethod
    def authenticate(email, password):
        user = User.query.filter(User.email == email).first()
        if user and user.check_password(password):
            return user
        return False
from app import db, bcrypt
from models import User
# from datetime import date # date_create=date.today()


def sample_data_db():
    """
    Populate a small db with some example entries.
    """
    exists = db.session.query(User.id).filter_by(email='test@test.com').first() is not None
    if (db.engine.has_table('user')) and (exists==False):
        
        import string
        import random

        db.drop_all()
        db.create_all()
        # test user
        password = bcrypt.generate_password_hash('test')
        test_user = User(email='test@test.com', password_hash=password)
        db.session.add(test_user)

        names = [
            'Harry', 'Amelia', 'Oliver', 'Jack', 'Isabella', 'Charlie','Sophie', 'Mia'
        ]

        for i in range(len(names)):
            user = User()
            user.name = names[i]
            user.email = user.name + "@example.com"
            user.password = bcrypt.generate_password_hash(''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(10)))
            db.session.add(user)

        db.session.commit()
        return        
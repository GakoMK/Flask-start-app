from manage import User
from app import app, db
import models
import views
import admin
import start

if __name__ == '__main__':    
    start.sample_data_db() # not working
    app.run(host='127.0.0.1', port=5000, debug=True) 
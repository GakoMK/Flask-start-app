from app import app
import models
import views
import admin


if __name__ == '__main__':
    # Start app  
    app.run(host='127.0.0.1', port=5000, debug=True) 
# Flask starter
A simple Flask app for a quick start. It contains the SQLite database, login, admin panel and test users in the database. <br/>
Layout based on Bootstrap 4<br/>
<br/>
<img src="https://github.com/GakoMK/Flask-start-app/blob/master/static/login.png">
<br/>
<img src="https://github.com/GakoMK/Flask-start-app/blob/master/static/front.png">
<br/>
<img src="https://github.com/GakoMK/Flask-start-app/blob/master/static/admin.png">
<br/>

Used in the project:<br/>
- flask_admin
- flask_login
- flask_migrate
- flask_sqlalchemy
- Bootstrap 4 (cdn)
<br/>
**This project was created while learning Flask, maybe it will be useful to someone.**

<br/>

## How to start:
1. Create folder 'data'
2. Python:
```
manage.py db init
manage.py db migrate
manage.py db upgrade
main.py
```
A database with a sample user (pass: test) will be created.
<br/>
3. Run main.py

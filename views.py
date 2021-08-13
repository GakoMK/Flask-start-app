from flask import render_template, redirect, url_for, request, flash, session, g
from flask_login import login_required
from app import app, db, login_manager
from flask_login.utils import login_user
from flask_login import login_user, login_required, logout_user, current_user
from models import User
from forms import LoginForm, RegisterForm


@app.route('/')
@login_required
def index():
    return render_template('index.html', title="Home page")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        form = LoginForm(request.form)
        if form.validate():
            login_user(form.user, remember=form.remember.data)
            flash("Successfully logged in as %s." % form.user.email, "success")
            return redirect(url_for('index'))
        else:
            flash('Try again!')
            return render_template('login.html', form=form) # przekazuje formularz do templatki
    else:
        form = LoginForm()
        return render_template('login.html', form=form) # przekazuje formularz do templatki


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        form = RegisterForm(request.form)
        new_user = User.create(email=form.email.data, password=form.password.data, name=form.name.data)
        db.session.add(new_user)
        db.session.commit()
        flash('New user has been created!')
        return redirect(url_for('login'))         
    else:
        form = RegisterForm()


@app.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(request.args.get('next') or url_for('index'))        


@app.before_request
def _before_request():
    g.user = current_user

# book
@login_manager.user_loader
def _user_loader(user_id):
    return User.query.get(int(user_id))
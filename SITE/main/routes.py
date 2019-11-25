from flask import render_template, request, redirect, url_for, flash
from main import app, db, bcrypt
from main.models import User, Link, Click
from main.forms import ExtendForm, LoginForm, RegisterForm
from flask_login import login_user




@app.route("/",methods=["GET","POST"])
@app.route("/<slink>")
def index(slink=None):
    if slink and slink[-1] is not '+':
        return render_template("index.html", title="Index", slink=slink)
    return redirect(url_for("home"))

@app.route("/home",methods=["GET","POST"])
def home():
    form = ExtendForm()
    if form.validate_on_submit():
        url = form.url.data[::-1]
        return render_template("home.html", url=url, title="Home", form=form)    
    return render_template("home.html", title="Home", form=form)    

@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash(f"Incorrect Email or Password!! ",'danger')
    return render_template("login.html", title="login", form=form)

@app.route("/register", methods=["GET","POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"You account has been created successfully!! ",'success')
        return redirect(url_for('login'))    
    return render_template("register.html", title="register", form=form)


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html",title="NOT FOUND")

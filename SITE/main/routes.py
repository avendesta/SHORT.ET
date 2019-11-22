from flask import render_template, request, redirect, url_for, flash
from main import app
from main.models import User, Link, Click
from main.forms import ExtendForm, LoginForm, RegisterForm




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
        flash(f"You have successfully logged in!! ",'success')
    return render_template("login.html", title="login", form=form)

@app.route("/register", methods=["GET","POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f"You have successfully registered!! ",'success')    
    return render_template("register.html", title="register", form=form)


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html",title="NOT FOUND")

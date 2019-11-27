from flask import render_template, request, redirect, url_for, flash, request
from short import app, db, bcrypt
from short.models import User, Link, Click
from short.forms import ExtendForm, LoginForm, RegisterForm, AddLinkForm
from flask_login import login_user, current_user, logout_user, login_required




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
        return render_template("home.html", url=url, title="Home", form=form, display=current_user.is_authenticated)    
    return render_template("home.html", title="Home", form=form,hide=current_user.is_authenticated)    

@app.route("/login", methods=["GET","POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home',title='Home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('account',title='Account'))
        else:
            flash(f"Incorrect Email or Password!! ",'danger')
    return render_template("login.html", title="login", form=form)

@app.route("/register", methods=["GET","POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home',title='Home',hide=True))

    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"You account has been created successfully!! ",'success')
        return redirect(url_for('login',title='Login'))    
    return render_template("register.html", title="register", form=form)


@app.route('/links',methods=["GET","POST"])
@login_required
def links():
    form = AddLinkForm()
    if form.validate_on_submit():
        link = Link(short_link=form.short_link.data, long_link=form.long_link.data,user_id=current_user.id)
        db.session.add(link)
        db.session.commit()
        flash("Link created successfully!",'success')
        return redirect(url_for('links',user=current_user,title='Links',form=form))
    return render_template('links.html',user=current_user,title='Links',form=form)

@app.route('/about')
def about():
    return "This is about page"

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have logged out successfully",'info')
    return redirect(url_for('home',title='Home'))

@app.route('/account')
@login_required
def account():
    return render_template('account.html',title='Account',current_user=current_user)


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html",title="NOT FOUND")

from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from forms import ExtendForm, LoginForm, RegisterForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "tHISiSsECRET"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    image_file = db.Column(db.String(40), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    links = db.relationship('Link',backref='creator', lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    short_link = db.Column(db.String(100), unique=True, nullable=False)
    long_link = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    clicks = db.relationship('Click',backref='stat',lazy=True)

    def __repr__(self):
        return f"Link('{self.short_link}','{self.long_link}','{self.date_created}')"

class Click(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, nullable=False, default=0)
    click_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    click_ip = db.Column(db.String(20), default='127.0.0.1')
    link_id = db.Column(db.Integer, db.ForeignKey('link.id'), nullable=False)

    def __repr__(self):
        return f"Click('{self.count}','{self.click_date}','{self.click_ip}')"


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


if __name__ == "__main__":
    app.run(debug=True)
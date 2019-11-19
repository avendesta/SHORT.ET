from flask import Flask, render_template, request, redirect, url_for, flash
from forms import ExtendForm, LoginForm, RegisterForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config["SECRET_KEY"] = "tHISiSsECRET"

@app.route("/",methods=["GET","POST"])
@app.route("/<slink>",methods=["GET","POST"])
def index(slink=None):
    if slink and slink[-1] is not '+':
        return render_template("index.html", title="Index", slink=slink)
    return redirect(url_for("home"))

@app.route("/home",methods=["GET","POST"])
def home():
    form = ExtendForm()
    if form.validate_on_submit():
        url = form.url.data
        return render_template("home.html", url=url, title="Home", form=form)    
    return render_template("home.html", title="Home", form=form)    

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", form=form)

@app.route("/register")
def register():
    form = RegisterForm()
    return render_template("register.html", form=form)


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html",title="NOT FOUND")


if __name__ == "__main__":
    app.run(debug=True)
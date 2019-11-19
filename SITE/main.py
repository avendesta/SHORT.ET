from flask import Flask, render_template, request, redirect, url_for, flash
from forms import ExtendForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)
# Bootstrap(app)
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
    url = ""
    if form.validate_on_submit():
        if request.method == "POST" and request.form.get('url'):
            url = request.form.get('url')
    return render_template("home.html", title="Home", url=url,form=form)


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(debug=True)
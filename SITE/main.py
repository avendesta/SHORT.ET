from flask import Flask, render_template, request, redirect, url_for
from forms import ExtendForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "tHISiSsECRET"
@app.route("/",methods=["GET"])
def index():
    if request.args.get('url'):
        url = request.args.get('url')
        return redirect(url)
    return redirect(url_for('home'))

@app.route("/home",methods=["GET","POST"])
def home():
    form = ExtendForm()
    if request.method == "POST" and request.form.get('url'):
        url = request.form.get('url')
    else:
        url = ""
    return render_template("home.html",url=url,form=form)

if __name__ == "__main__":
    app.run(debug=True)
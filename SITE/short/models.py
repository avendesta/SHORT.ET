from datetime import datetime
from short import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
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
    count = db.Column(db.Integer, nullable=False, default=0)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_destroyed = db.Column(db.DateTime, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    clicks = db.relationship('Click',backref='stat',lazy=True)

    def __repr__(self):
        return f"Link('{self.short_link}','{self.long_link}','{self.date_created}')"

class Click(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    click_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    click_ip = db.Column(db.String(20), default='127.0.0.1')
    link_id = db.Column(db.Integer, db.ForeignKey('link.id'), nullable=False)

    def __repr__(self):
        return f"Click('{self.click_date}','{self.click_ip}','{self.link_id}')"

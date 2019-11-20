from main import db
from main import User, Link, Click

db.create_all()
user_1 = User(username="Rick",email="RS@gmail.com",password="AdultSwim")
user_2 = User(username="Homer",email="Simpson@gmail.com",password="Fox")

db.session.add(user_1)
db.session.add(user_2)
db.session.commit()

print("SHOWING All users")
User.query.all()

link_1 = Link(short_link='x.et/hexo', long_link='https://www.google.com/', user_id=first.id)
link_2 = Link(short_link='x.et/love', long_link='https://www.yahoo.com/', user_id=first.id)
link_3 = Link(short_link='x.et/moon', long_link='https://www.yandex.com/', user_id=second.id)
db.session.add(link_1)
db.session.add(link_2)
db.session.add(link_3)
db.session.commit()


click_1 = Click(count=9, click_ip='132.43.23.5', link_id=link_1.id)
click_2 = Click(count=7, click_ip='132.43.23.5', link_id=link_2.id)
click_3 = Click(count=5, click_ip='132.43.23.5', link_id=link_2.id)
click_4 = Click(link_id=link_3.id)
db.session.add(click_1)
db.session.add(click_2)
db.session.add(click_3)
db.session.add(click_4)
db.session.commit()

print("Queries\n\n")

user_1.username
user_2.links
link_1.short_link
link_2.long_link
link_3.clicks
click_1.count
click_2.click_ip
click_3.click_date
click_4
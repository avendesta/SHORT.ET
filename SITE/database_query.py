from short import db
from short.models import User, Link, Click

db.create_all()

user_1 = User(username="Rick",email="RS@gmail.com",password="$2b$12$lQbF5qi6u5gfj3stT606e.d/TgVgBajb9LX.Q5yS/RNeIqbawEn8i")
user_2 = User(username="Homer",email="Simpson@gmail.com",password="$2b$12$lQbF5qi6u5gfj3stT606e.d/TgVgBajb9LX.Q5yS/RNeIqbawEn8i")
print("Password is 12345678")

db.session.add(user_1)
db.session.add(user_2)
db.session.commit()

print("SHOWING All users")
User.query.all()

link_1 = Link(short_link='x.et/hexo', long_link='https://www.google.com/', user_id=user_1.id)
link_2 = Link(short_link='x.et/love', long_link='https://www.yahoo.com/', user_id=user_1.id)
link_3 = Link(short_link='x.et/moon', long_link='https://www.yandex.com/', user_id=user_2.id)
db.session.add(link_1)
db.session.add(link_2)
db.session.add(link_3)
db.session.commit()


click_1 = Click(click_ip='11.43.23.5', link_id=link_1.id)
click_2 = Click(click_ip='12.3.3.8', link_id=link_2.id)
click_3 = Click(click_ip='20.43.23.5', link_id=link_2.id)
click_4 = Click(click_ip='8.8.8.8', link_id=link_2.id)
click_5 = Click(link_id=link_3.id)
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
link_1.date_created
link_2.date_destroyed
link_3.count
link_3.clicks
click_1
click_2.click_ip
click_3.click_date
click_4

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.cfg')


subs = db.Table(
    'subs',
    db.Column(
        'user_id',
        db.Integer,
        db.ForeignKey('user.user_id')),
    db.Column(
        'channel_id',
        db.Integer,
        db.ForeignKey('channel.channel_id')))


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    subscriptions = db.relationship(
        'Channel', secondary=subs, backref=db.backref(
            'subscribers', lazy='dynamic'))


class Channel(db.Model):
    channel_id = db.Column(db.Integer, primary_key=True)
    channel_name = db.Column(db.String(20))


db.create_all()

user1 = User(name='Anthony')
user2 = User(name='Stacy')
user3 = User(name='George')
user4 = User(name='Amber')

db.session.add(user1, user2, user3, user4)

channel1 = Channel(channel_name='Pretty Printed')
channel2 = Channel(channel_name='Cat Videos')

db.session.add(channel1, channel2)

channel1.subscribers.append(user1, user3, user4)
channel2.subscribers.append(user2, user4)

db.session.commit()

channel1.subscribers
for user in channel1.subscribers:
    print(user.name)

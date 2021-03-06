# coding:utf-8
'''
models
'''

from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

posts_tags = db.Table('posts_tags', db.Column('post_id', db.String(45),
                                              db.ForeignKey('posts.id')),
                      db.Column('tag_id', db.String(45),
                                db.ForeignKey('tags.id')))  # opqa


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(45), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    posts = db.relationship('Post', backref='users', lazy='dynamic')

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        '''define the string format for instance of User.'''
        return '<Model User: %r>' % self.username


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.String(45), primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime)
    # set the foreign key for Post
    user_id = db.Column(db.String(45), db.ForeignKey('users.id'))

    # establish contact with Comment's ForeignKey: post_id
    comments = db.relationship('Comment', backref='posts', lazy='dynamic')
    # many to many : posts <=> tags
    tags = db.relationship('Tag', secondary=posts_tags,
                           backref=db.backref('posts', lazy='dynamic'))  # noqa

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<Model Post %r>' % self.title


class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Model Tag: %r>' % self.name


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(255))
    text = db.Column(db.Text())
    data = db.Column(db.DateTime())
    post_id = db.Column(db.String(45), db.ForeignKey('posts.id'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Model Comment %r>' % self.name

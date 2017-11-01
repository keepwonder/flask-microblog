# coding:utf-8
'''
config file
'''


class Config(object):
    """Base config class."""
    pass


class ProdConfig(Config):
    """Production config class."""
    pass


class DevConfig(Config):
    """Development config class."""
    # open the DEBUG
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/db_for_microblog'# noqa
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# coding:utf-8
'''
it's a shell management script
'''

from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app import app
from models import db, User, Post, Comment, Tag

# Init manager object via app object
manager = Manager(app)

# Init migrate object via app and db object
migrate = Migrate(app, db)

# Create some new commands
manager.add_command('server', Server())
manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
    """Create a python CLI.

    return: Default import object
    type: `Dcit`
    """
    # 确保有导入Flask app obejct,否则启动的CLI上下文中仍然没有app对象
    return dict(app=app, db=db, User=User, Post=Post, Comment=Comment, Tag=Tag)


if __name__ == '__main__':
    manager.run()

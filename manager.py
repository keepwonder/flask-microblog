# coding:utf-8

from flask_script import Manager, Server
from app import app
from models import db, User

manager = Manager(app)
manager.add_command('server', Server())

@manager.shell
def make_shell_context():
    """Create a python CLI.

	return: Default import object
	type: `Dcit`
	"""
	# 确保有导入Flask app obejct,否则启动的CLI上下文中仍然没有app对象
    return dict(app=app, db=db, User=User)

if __name__ == '__main__':
    manager.run()

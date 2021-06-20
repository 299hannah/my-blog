import os
from app import create_app,db
from app.models import User,Post
from  flask_migrate import Migrate, MigrateCommand
from flask_script import Manager,Server

app = create_app('development')

#creating app instance
manager = Manager(app)
manager.add_command('server',Server)
@manager .command
def test():
    '''
    Run the unit tests
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.shell
def make_shell_contex():
    return dict(app=app, db=db, User=User, Post=Post)


migrate = Migrate(app,db)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
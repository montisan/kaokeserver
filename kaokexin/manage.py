#!/usr/bin/env python3
import os
from app import create_app, db
from app.models import Admin, Role, User, Set, Item, Order
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app,db)

def make_shell_context():
	return dict(app=app, db=db, User=User, Role=Role, Admin=Admin, Set=Set, Item=Item, Order=Order)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()
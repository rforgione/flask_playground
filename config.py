import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app/data/app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'app/data/db_repository')

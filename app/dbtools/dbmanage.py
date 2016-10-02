from migrate.versioning import api
from app import db, config
import os.path
import imp

class DBTools_DBManage(object):

    def __init__(self):
        pass

    def db_create(self):
        db.create_all()
        if not os.path.exists(config.SQLALCHEMY_MIGRATE_REPO):
            api.create(config.SQLALCHEMY_MIGRATE_REPO, 'database repository')
            api.version_control(config.SQLALCHEMY_DATABASE_URI, config.SQLALCHEMY_MIGRATE_REPO)
        else:
            api.version_control(config.SQLALCHEMY_DATABASE_URI, config.SQLALCHEMY_MIGRATE_REPO, api.version(config.SQLALCHEMY_MIGRATE_REPO))

    def db_upgrade(self):
        api.upgrade(config.SQLALCHEMY_DATABASE_URI, config.SQLALCHEMY_MIGRATE_REPO)
        v = api.db_version(config.SQLALCHEMY_DATABASE_URI, config.SQLALCHEMY_MIGRATE_REPO)
        print('Current database version: ' + str(v))

    def db_downgrade(self):
        v = api.db_version(config.SQLALCHEMY_DATABASE_URI, config.SQLALCHEMY_MIGRATE_REPO)
        api.downgrade(config.SQLALCHEMY_DATABASE_URI, config.SQLALCHEMY_MIGRATE_REPO, v - 1)
        v = api.db_version(config.SQLALCHEMY_DATABASE_URI, config.SQLALCHEMY_MIGRATE_REPO)
        print('Current database version: ' + str(v))

    def db_migrate(self):
        v = api.db_version(config.SQLALCHEMY_DATABASE_URI, config.SQLALCHEMY_MIGRATE_REPO)
        migration = config.SQLALCHEMY_MIGRATE_REPO + ('/versions/%03d_migration.py' % (v+1))
        tmp_module = imp.new_module('old_model')
        old_model = api.create_model(config.SQLALCHEMY_DATABASE_URI, config.SQLALCHEMY_MIGRATE_REPO)
        exec(old_model, tmp_module.__dict__)
        script = api.make_update_script_for_model(config.SQLALCHEMY_DATABASE_URI, config.SQLALCHEMY_MIGRATE_REPO, tmp_module.meta, db.metadata)
        open(migration, "wt").write(script)
        api.upgrade(config.SQLALCHEMY_DATABASE_URI, config.SQLALCHEMY_MIGRATE_REPO)
        v = api.db_version(config.SQLALCHEMY_DATABASE_URI, config.SQLALCHEMY_MIGRATE_REPO)
        print('New migration saved as ' + migration)
        print('Current database version: ' + str(v))

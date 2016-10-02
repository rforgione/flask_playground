# from dbtools.dbmanage import DBTools_DBManage
from sys import argv
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from app import app
from app.dbtools.dbmanage import DBTools_DBManage

dbmanage = DBTools_DBManage()

if argv[1] == 'create':
    dbmanage.db_create()
elif argv[1] == 'upgrade':
    dbmanage.db_upgrade()
elif argv[1] == 'downgrade':
    dbmanage.db_downgrade()
elif argv[1] == 'migrate':
    dbmanage.db_migrate()

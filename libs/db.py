__author__ = 'brlnt-super'

import MySQLdb

import config


configuration = config.get()
defaultdb = configuration.get('default').get('db')

def connect(isfirst = False):
    if isfirst:
        return MySQLdb.connect(
            host=configuration.get(defaultdb).get('host'),
            port=configuration.get(defaultdb).get('port'),
            user=configuration.get(defaultdb).get('username'),
            passwd=configuration.get(defaultdb).get('password')
        )
    else:
        return MySQLdb.connect(
            host=configuration.get(defaultdb).get('host'),
            port=configuration.get(defaultdb).get('port'),
            user=configuration.get(defaultdb).get('username'),
            passwd=configuration.get(defaultdb).get('password'),
            db=configuration.get(defaultdb).get('database')
        )

def insert():
    pass

def update():
    pass

def delete():
    pass

def get():
    pass

def execute():
    pass
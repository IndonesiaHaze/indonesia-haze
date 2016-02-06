__author__ = 'brlnt-super'

from enum import Enum
import MySQLdb
import config



configuration = config.get()
defaultdb = configuration.get('default').get('db')


class Qtype(Enum):
    C = None
    R = None
    U = None
    D = None


def connect(isfirst=False):
    """
    Function to establish mysql connection
    :param isfirst: true if first install, false if its not first install
    :return: MySQL connection
    """
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


def insert(data, **kwargs):
    """
    :param data: the data that need to be inserted, dict()
    :param kwargs: * dbcon: database connection
    :return: * bool: is execution success or not
    """
    if type(data) == dict:
        for name, arg in kwargs.items():
            if name == 'dbcon':
                con = arg
        query = __querybuilder(type=Qtype.C, data=data)

        result = execute(query)


def update(id, data, **kwargs):
    pass


def delete(data, **kwargs):
    pass


def get(id, table, **kwargs):
    pass


def execute(query, **kwargs):
    result = None
    if type(query) == str:
        con = connect()
        for name, arg in kwargs.items():
            if name == 'dbcon':
                con = arg

        cur = con.cursor()
        cur.execute(query)

        con.close()

    return result


def __querybuilder(**kwargs):
    query = ""
    return query
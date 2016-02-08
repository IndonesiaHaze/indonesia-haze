__author__ = "brlnt-super"

from enum import Enum
import MySQLdb

import config


class Qtype(Enum):
    """Defined query type"""
    C = None
    R = None
    U = None
    D = None
    Custom = None


class DbConnection():
    def __init__(self):
        self.configuration = config.get()
        self.defaultdb = self.configuration.get("default").get("db")
        pass

    def connect(self, isfirst=False):
        """Establish mysql connection
        :param isfirst: true if first install, false if its not
        :return: MySQL connection
        """
        if isfirst:
            return MySQLdb.connect(
                host=self.configuration.get(self.defaultdb).get("host"),
                port=self.configuration.get(self.defaultdb).get("port"),
                user=self.configuration.get(self.defaultdb).get("username"),
                passwd=self.configuration.get(self.defaultdb).get("password")
            )

        return MySQLdb.connect(
            host=self.configuration.get(self.defaultdb).get("host"),
            port=self.configuration.get(self.defaultdb).get("port"),
            user=self.configuration.get(self.defaultdb).get("username"),
            passwd=self.configuration.get(self.defaultdb).get("password"),
            db=self.configuration.get(self.defaultdb).get("database")
        )


class DbTransaction():
    def __init__(self):
        pass

    def tran(self, data=None, qtype=Qtype.Custom, dbcon=DbConnection().connect()):
        """interface for processing data
        :param data:
        :param qtype:
        :param dbcon:
        :return:
        """
        if type(data).__name__ == "instance":
            # Make sure the data is an instance of object
            query = self._querybuilder(qtype=qtype, data=data)
            result = self.execute(query=query, qtype=qtype, dbcon=dbcon)
            return result

        return None

    def execute(self, query, qtype, dbcon):
        """Execute query from defined one
        :param query: executable string query for sql
        :param dbcon: database connection (MySQLdb)
        :return: cursor object
        """

        if type(query).__name__ == 'str' \
                and qtype is not None \
                and dbcon is not None:
            con = dbcon
            cur = con.cursor()
            cur.execute(query)

            if qtype != Qtype.R:
                con.commit()

            con.close()
            return cur

        return None

    def _querybuilder(self, qtype, data):
        """Return the query string from the object model
        and desirable query type (C, R, U, D, Custom)
        :param qtype: query type
        :param data: object model
        :return: query string
        """
        query = ""

        if qtype is not None and data is not None:
            cls = data.__class__
            clsname = cls.__name__

            if qtype == Qtype.C:
                # query insert
                query = self._qry_insert(cls, clsname)
            elif qtype == Qtype.R:
                pass
            elif qtype == Qtype.U:
                pass
            elif qtype == Qtype.D:
                pass
            elif qtype == Qtype.Custom:
                pass

        return query

    def _qry_insert(self, cls, clsname):
        """Generate insert query from defined class object
        :param cls: class object
        :param clsname: class name
        :return: query string
        """
        query = ""
        obj = self._getfields(cls.__dict__)

        if len(obj) != 0:
            # object not empty
            query = "INSERT INTO "+clsname+" SET "
            for i, field in enumerate(obj):
                tqry = " %s = '%s'"
                query += tqry % (field, obj[field])

                if i < len(obj)-1:
                    query += ","

        return query

    def _getfields(self, obj, nullable=False):
        """Get all field from object model
        :param obj: object model
        :param nullable: indicator for including null(None) object
        :return:
        """
        result = dict()
        for key, value in obj.items():
            if key[0] != '_':
                if value is None:
                    if nullable:
                        value = 'NULL'
                        result[key] = value
                else:
                    result[key] = value

        return result


def insert(**kwargs):
    """Insert data to database
    :param kwargs:
    :return:
    """
    return DbTransaction().tran(qtype=Qtype.C, **kwargs)


def update(**kwargs):
    pass


def delete(**kwargs):
    pass


def getdata(**kwargs):
    pass


def getdatas(**kwargs):
    pass
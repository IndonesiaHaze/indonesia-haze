__author__ = "brlnt-super"

from enum import Enum

from dbc import DbConnection


class Qtype(Enum):
    """Defined query type"""
    C = None
    R = None
    U = None
    D = None
    Custom = None


class DbTransaction():
    def __init__(self, data=None, qtype=Qtype.Custom, dbcon=None, query=None):
        """
        :param data:
        :param qtype:
        :param dbcon:
        :return:
        """
        self.data = data
        self.qtype = qtype
        self.dbcon = dbcon
        self.query = query
        self.result = None

    def tran(self):
        """

        :return:
        """
        self.query = self._querybuilder()
        self.result = self.execute()

        return self.result

    def execute(self):
        """Execute query from defined one
        :return: cursor object
        """
        if self.dbcon is None:
            self.dbcon = DbConnection().connect()

        if type(self.query).__name__ == 'str' \
                and self.query is not None \
                and self.qtype is not None \
                and self.dbcon is not None:
            con = self.dbcon
            cur = con.cursor()
            cur.execute(self.query)

            if self.qtype != Qtype.R:
                con.commit()

            con.close()
            return cur

        return None

    def _querybuilder(self):
        """Return the query string from the object model
        and desirable query type (C, R, U, D, Custom)
        :return: query string
        """
        query = None
        if self.qtype is not None and self.data is not None:
            cls = self.data.__class__
            clsname = cls.__name__

            if self.qtype == Qtype.C:
                # query insert
                query = self._qry_insert(self.data, clsname)
            elif self.qtype == Qtype.R:
                pass
            elif self.qtype == Qtype.U:
                pass
            elif self.qtype == Qtype.D:
                pass
            elif self.qtype == Qtype.Custom:
                pass

        return query

    def _qry_insert(self, cls, clsname):
        """Generate insert query from defined class object
        :param cls: class object
        :param clsname: class name
        :return: query string
        """
        query = None
        obj = self._getfields(cls.__dict__)

        if len(obj) != 0:
            # object not empty
            query = "INSERT INTO "+clsname+" SET"
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
    :return: cursor or None
    """
    return DbTransaction(qtype=Qtype.C, **kwargs).tran()


def update(**kwargs):
    pass


def delete(**kwargs):
    pass


def getdata(**kwargs):
    pass


def getdatas(**kwargs):
    pass

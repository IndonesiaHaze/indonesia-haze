__author__ = 'brlnt-super'

import MySQLdb

from conf import config


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
        else:
            return MySQLdb.connect(
                host=self.configuration.get(self.defaultdb).get("host"),
                port=self.configuration.get(self.defaultdb).get("port"),
                user=self.configuration.get(self.defaultdb).get("username"),
                passwd=self.configuration.get(self.defaultdb).get("password"),
                db=self.configuration.get(self.defaultdb).get("database")
            )
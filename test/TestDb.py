__author__ = 'brlnt-super'

import unittest

import mock


class TestDb(unittest.TestCase):
    def _getTarget(self):
        from libs import db
        return db

    def _makeOne(self, **kw):
        self.dbobj = self._getTarget().DbTransaction(**kw)
        return self.dbobj.tran()

    def _makeDbCon(self):
        import MySQLdb
        mockcon = mock.create_autospec(MySQLdb)
        return mockcon.connect()

    def test_dbInsert_IfDataIsNull_ReturnNoneValue(self):
        from models.Hotspot import Hotspot
        data = Hotspot()
        result = self._makeOne(qtype=self._getTarget().Qtype.C, dbcon=self._makeDbCon(), data=data)
        self.assertEqual(result, None)
        self.assertEqual(self.dbobj.query, None)

    def test_dbInsert_IfDataNotNull_ReturnCursor(self):
        from models.Hotspot import Hotspot
        data = Hotspot()
        data.Confidence = 1
        data.HotspotID = 3
        result = self._makeOne(qtype=self._getTarget().Qtype.C, dbcon=self._makeDbCon(), data=data)
        self.assertNotEqual(result, None)
        self.assertEqual(self.dbobj.query, "INSERT INTO Hotspot SET Confidence = '1', HotspotID = '3'")

if __name__ == '__main__':
    unittest.main()

__author__ = 'brlnt-super'
import urllib2

class Connection:
    def __init__(self):
        pass

    @staticmethod
    def getdata(url):
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)

        return response.read()
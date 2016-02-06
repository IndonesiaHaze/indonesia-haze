__author__ = 'brlnt-super'
import urllib2

def getDataBmkg(url):
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)

    return response.read()
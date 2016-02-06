__author__ = 'brlnt-super'
import urllib2


def get(url):
    """Return string data from called url

    For webservice with get method
    """
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)

    return response.read()
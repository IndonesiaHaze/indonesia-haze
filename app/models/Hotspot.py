__author__ = 'brlnt-super'

from enum import Enum


class Hotspot():
    HotspotID = None
    Longitude = None
    Latitude = None
    Confidence = None
    Region = None
    Provinsi = None
    Kabupaten = None
    Kecamatan = None
    EntryDate = None
    LastUpdatedTime = None

    def __init__(self):
        pass

    def pk(self):
        return ['HotspotID']
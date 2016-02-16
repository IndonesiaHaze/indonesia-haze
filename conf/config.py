__author__ = 'brlnt-super'

import ConfigParser
import io
import os


def get():
    """Get configuration file from config.ini
    :return: configuration in dictionary
    """
    with open(os.path.abspath("..\\config.ini")) as f:
        configs = f.read()

    config = ConfigParser.RawConfigParser(allow_no_value=True)
    config.readfp(io.BytesIO(configs))

    confs = dict()

    # List all contents
    for section in config.sections():
        conf = dict()
        for options in config.options(section):
            conf[options] = config.get(section, options)
        confs[section] = conf

    return confs
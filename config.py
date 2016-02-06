__author__ = 'brlnt-super'

import ConfigParser
import io


def get():
    # Load the configuration file
    with open("..\\config.ini") as f:
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
__author__ = 'brlnt-super'

import ConfigParser
import io


def get():
    """Get configuration file from config.ini
    :return: configuration in dictionary
    """
    with open("..\\config.ini") as f:
        configs = f.read()

    config = ConfigParser.RawConfigParser(allow_no_value=True)
    config.readfp(io.BytesIO(configs))

    confs = dict()

    # List all contents
    for section in config.sections():
        conf = dict()
        for options in config.options(section):
            conf.update(options, config.get(section, options))
        confs.update(section, conf)

    return confs
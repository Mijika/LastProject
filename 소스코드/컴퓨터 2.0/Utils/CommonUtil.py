import os
import logging

from PyQt5.QtCore import QSettings, QTextCodec
from Utils.Confing import LogName, LogFormatterDebug, LogFormatter

def initLog(name, file=None, level=logging.DEBUG, formatter=None):
    """
    :param name:            log name
    :param file:            log file
    :param level:           log level
    :param formatter:       log formatter
    """

    formatter = formatter or logging.Formatter(
        LogFormatterDebug if level == logging.DEBUG else LogFormatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    if file != None:
        file = os.path.abspath(str(file))
        file_handler = logging.FileHandler(file, mode='w', encoding='utf-8')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

AppLog = logging.getLogger(LogName)

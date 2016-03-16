import sys
from humble_api.events import Events

__author__ = "Brian Schkerke"
__copyright__ = "Copyright 2016 Brian Schkerke"
__license__ = "MIT"


class EventHandler(object):
    @staticmethod
    def initialize():
        Events.on(Events.EVENT_MD5_START, EventHandler.print_md5_start)
        Events.on(Events.EVENT_MD5_END, EventHandler.print_md5_end)
        Events.on(Events.EVENT_DOWNLOAD_START, EventHandler.print_download_start)
        Events.on(Events.EVENT_DOWNLOAD_END, EventHandler.print_download_end)
        Events.on(Events.EVENT_PROGRESS, EventHandler.print_progress)

    @staticmethod
    def print_md5_start(filename):
        sys.stdout.write("[     MD5] %s: " % filename)

    @staticmethod
    def print_md5_end(filename):
        print ""

    @staticmethod
    def print_download_start(filename):
        sys.stdout.write("[Download] %s: " % filename)

    @staticmethod
    def print_download_end(filename):
        print ""

    @staticmethod
    def print_progress(percentage):
        sys.stdout.write("{0:.0f}% ".format(percentage))

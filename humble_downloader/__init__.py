#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import humble_downloader.logger as logger
from humble_downloader.config_data import ConfigData
from .configuration import Configuration
from .event_handler import EventHandler
from .humble_api.humble_api import HumbleApi
from .actions import Action

__author__ = "Brian Schkerke"
__copyright__ = "Copyright 2016 Brian Schkerke"
__license__ = "MIT"

__all__ = ["ConfigData", "Action", "display_message", "HumbleDownload", "ProgressTracker"]


def main():
    print("Humble Bundle Downloader v%s" % ConfigData.VERSION)
    print("This program is not affiliated nor endorsed by Humble Bundle, Inc.")
    print("For any suggestion or bug report, please create an issue at:\n%s" %
          ConfigData.BUG_REPORT_URL)
    print("")

    # Load the configuration from the YAML file...
    Configuration.load_configuration("hb-downloader-settings.yaml")
    Configuration.parse_command_line()
    Configuration.dump_configuration()
    Configuration.push_configuration()

    validation_status, message = Configuration.validate_configuration()
    if not validation_status:
        logger.display_message(False, "Error", message)
        sys.exit("Invalid configuration.  Please check your command line "
                 "arguments and hb-downloader-settings.yaml.")

    # Initialize the event handlers.
    EventHandler.initialize()

    hapi = HumbleApi(ConfigData.auth_sess_cookie)

    if not hapi.check_login():
            exit("Login to humblebundle.com failed."
                 "  Please verify your authentication cookie")

    logger.display_message(False, "Processing", "Downloading order list.")
    if ConfigData.restrict_keys:
        game_keys = ConfigData.restrict_keys
    else:
        game_keys = hapi.get_gamekeys()
    logger.display_message(False, "Processing", "%s orders found." %
                           (len(game_keys)))

    if ConfigData.action == "download":
        Action.batch_download(hapi, game_keys)
    else:
        Action.list_downloads(hapi, game_keys)


if __name__ == "__main__":
    sys.exit(main())

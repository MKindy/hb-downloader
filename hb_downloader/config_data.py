#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Brian Schkerke"
__copyright__ = "Copyright 2020 Brian Schkerke"
__license__ = "MIT"


class ConfigData(object):
    VERSION = "0.6.0"
    BUG_REPORT_URL = "https://github.com/talonius/hb-downloader/issues"
    action = ""
    print_url = False
    download_location = ""
    folderstructure_OrderName = True
    debug = False
    auth_sess_cookie = ""
    write_md5 = True
    read_md5 = True
    force_md5 = False
    chunk_size = 8192000
    ignore_md5 = False
    resume_downloads = True
    download_product = "-not specified-"
    get_extra_file_info = False
    config_filename = "hb-downloader-settings.yaml"
<<<<<<< HEAD
<<<<<<< HEAD
    
=======

>>>>>>> ced77c22d6cd2978ec4fd0902d284a7c8b480226
=======
    max_file_size = None
    file_extensions = None

>>>>>>> c1e499a9300dccfea9f58b12a80eabf0502fe75a
    download_platforms = {
        'audio': True,
        'ebook': True,
        'windows': True,
        'mac': True,
        'linux': True,
        'android': True,
        'asmjs': False
    }

    audio_types = {
        "flac": True,
        "ogg": True,
        "mp3": True,
        "other": True
    }

    ebook_types = {
        "epub": True,
        "pdf": True,
        "mobi": True,
        "other": True
    }

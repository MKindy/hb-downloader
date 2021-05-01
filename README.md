# hb-downloader
[![Coverage Status](https://coveralls.io/repos/github/MKindy/hb-downloader/badge.svg)](https://coveralls.io/github/MKindy/hb-downloader)
[![Build Status](https://travis-ci.org/MKindy/hb-downloader.svg)](https://travis-ci.org/MKindy/hb-downloader)

An automated utility to download your Humble Bundle purchases.

    http://www.humblebundle.com

This package is not endorsed, supported, or affiliated with Humble Bundle, Inc.

It is distributed under the MIT license. You may use, modify, and redistribute it freely provided you agree with the terms of the license, found in the accompanying LICENSE file or online at [https://opensource.org/licenses/MIT](https://opensource.org/licenses/MIT).

This is a fork with additional functionality and fixes of the software originally distributed by Brian Schkerke and available at [https://github.com/talonius/hb-downloader](https://github.com/talonius/hb-downloader).

This repository contains code from Joel Pedraza's awesome `humblebundle-python` library, available at [https://github.com/saik0/humblebundle-python](https://github.com/saik0/humblebundle-python).

## Requirements
* Python 3.6
* requests library
* pyyaml library
* lxml _(optional, for Humble Trove support)_

## Python Installation
Several features particular to Python v3.6 might have been used during the development of this script.  To install Python v3.6 visit [https://www.python.org/downloads/](https://www.python.org/downloads/) and grab the latest 3.x.x release.

## Getting the Prerequisites
From the command line, run the command:

    pip install requests pyyaml lxml

You'll either be informed that the requirement is already satisfied, or `pip` will retrieve, install, and configure the libraries for you.

Alternatively, you can run the `setup.py` script.

## Getting the Script Files
Perform one of the following actions:
* Download the latest code from the [master branch](https://github.com/MKindy/hb-downloader/archive/master.zip) as a zip file; or
* Check out the source with Git: `git clone https://github.com/MKindy/hb-downloader.git`

## Configuring the Script
`hb-downloader-settings.yaml` is the configuration file for the script.  It contains all of the information that can be overridden during script execution trough the command line interface. The format is:

    <variable name>: <variable value>

Or:

    <variable group>:
      <variable name>: <variable value>

The first thing you will need is to fetch your authentication cookie from humblebundle.com.  To do so, open [https://www.humblebundle.com/](https://www.humblebundle.com/), log in, and once logged in press F12 to open your browser's developer tools:
* In Firefox's Developer Tools, select the "Storage" tab and there look for the "Cookies" drop-down menu;
* In Chrome's Developer Tools, select the "Application" tab and there look for the "Cookies" drop-down menu under the "Storage" menu;
  * Safari, Opera, Vivaldi, Brave, and Edge will have similar layouts to Chrome;
  * Safari's developer tools must be separately enabled, as explained in the [online Safari User Guide](https://support.apple.com/guide/safari/use-the-developer-tools-in-the-develop-menu-sfri20948/mac);
* In Internet Explorer, navigate to your preference of either [https://mozilla.org/firefox/](https://mozilla.org/firefox/) or [https://google.com/chrome/](https://google.com/chrome/), install your new chosen browser, and then follow the steps above;
* In any of a number of alternative browser engines, you're on your own, but you'll probably figure it out fine, since you're the kind of enthusiast who's using a browser with essentially no market share;

Select the cookie for `https://www.humblebundle.com` and look for the variable named `_simple_auth` and copy its value, which will look like:
```pwsh
    <92-digit alphanumeric (base 62) number>|<10-digit decimal number>|<40-digit hexadecimal number>
```

Paste this value in single quotes in the `session-cookie` setting of the `hb-downloader-settings.yaml` file. You may alternatively choose to specify it on the command line with the `-c` flag, being sure to escape the `|` character accordingly.

`download-location` is where you want the files to be stored as and after they are downloaded.  This location needs to already exist and be writable by the user executing the script.  It can be a Linux-style directory (`/mnt/mark/Downloads/Humble`), a shared folder via a UNC path (`\\192.168.0.2\mark\Downloads\Humble`) or a Windows-style directory (`Z:\mark\Downloads\Humble`).

As configured, the settings file will tell the script to download every file in your Humble library. You may make further modifications to the `max-file-size` setting or to any or all of the `download-platforms`, `audio_types`, `ebook_types`, and/or `file-extensions` variable group settings to limit what gets downloaded.  It is unlikely you will need to make changes to any of the other settings.

## Issues
If you encounter any issues or have suggestions, please [open a new issue](https://github.com/MKindy/hb-downloader/issues) on GitHub.

## Known Issues
If you run the script in a Windows terminal or PowerShell session, you may encounter this error:
```pwsh
     UnicodeEncodeError: 'charmap' codec can't encode character...
```

This only happens if you have an extended character in the name of one of your products.  The easiest fix is to export an environment variable so that Python knows the terminal can accept Unicode; in your Windows terminal or PowerShell session, run:
```pwsh
# "set" defines the environment variable immediately, without persistence
set PYTHONIOENCODING=UTF-8
# "setx" permanently defines the environment variable, but requires restart
#    without "set" above:
setx PYTHONIOENCODING=UTF-8
```

## Usage examples
```pwsh
# Both of these will just download all the stuff according to your config files:
hb-downloader.py
hb-downloader.py download

# Lists all your products (the bundles) and subproducts (the individual titles):
hb-downloader.py list

# Will download a single bundle either from email link or game-key:
hb-downloader.py download-product <bundle url>
hb-downloader.py download-product <product key>
```

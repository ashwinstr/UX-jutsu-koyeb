# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/uaudith/Userge/blob/master/LICENSE >
#
# All rights reserved.

import os

""" req = open("requirements.txt", "r").readlines()

for one in req:
    try:
        os.system(f"pip install {one}")
    except Exception as e:
        print(f"Installing {one} failed - {e}")
 """
# os.system("pip3 install -U pip")
os.system("pip install -U -r requirements.txt")
os.system("export PATH='$PATH:/usr/local/lib/python3.10' && ls usr/local/lib/python3.10")
# os.system("pip install git+https://github.com/ashwinstr/pyrogram@x21")
# os.system("pip install pymongo[srv]")
# os.system("pip install gitpython")
# os.system("pip install requests"))

import sys
print(sys.path)
print(sys.executable)

from userge.logger import logging  # noqa
from userge.config import Config, get_version  # noqa
from userge.fonts import Font
from userge.core import (  # noqa
    Userge, filters, Message, get_collection, pool)

userge = Userge()  # userge is the client name

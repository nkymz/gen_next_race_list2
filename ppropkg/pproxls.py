# -*- coding: utf-8 -*-

import os
import re
import datetime
import time

import openpyxl
import requests
from bs4 import BeautifulSoup

PPRO_PATH = os.getenv("HOMEDRIVE", "None") + os.getenv("HOMEPATH", "None") + "/Dropbox/POG/"






wbpath = (path + "POG_HorseList.xlsx").replace("\\", "/")
htmlpath = (path + "PO_race_horse_list.html").replace("\\", "/")




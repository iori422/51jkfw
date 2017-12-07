# -*- coding: utf-8 -*-
from  selenium import webdriver
from distutils.core import setup
import py2exe

includes = ["encodings", "encodings.*"]
options = {"py2exe":
             {   "compressed": 1,
                 "optimize": 2,
                 "includes": includes,
                 "bundle_files": 1
             }
           }
setup(
     version = "0.1.0",
     description = "windows program",
     name = "winsetup",
     options = options,
     zipfile=None,
     windows=[{"script": "myscript.py", "icon_resources": [(1, "PyCrust.ico")] }],
  )
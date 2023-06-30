#!/usr/bin/env python3
# 

import shutil
import requests
import os
from pathlib import Path

url = 'https://raw.githubusercontent.com/0xSteady/minionsparser.py/main/minionsparser.py'
response = requests.get(url)

output = open("/usr/src/app/minionsparser.py", "w")
output.writelines(response.text)

print('The file was saved successfully')

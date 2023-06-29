#!/usr/bin/env python3
# 
# Description: This script normalizes the data contained in the file published by 
# Binary Edge at https://api.binaryedge.io/v1/minions into a format that can be 
# consumed as an EDL by the Palo Alto NGFW
#
# SUPPORT POLICY
# 
# This script is provided under an AS-IS, best effort, support policy. 
# These scripts should be seen as community supported and Palo Alto Networks will 
# contribute our expertise as and when possible. We do not provide technical support 
# or help in using or troubleshooting the components of the project through our 
# normal support options such as Palo Alto Networks support teams, or ASC (Authorized 
# Support Centers) partners and backline support options. 
#
# The underlying product used (the NGFW and EDLs) by the scripts is still supported, 
# but the support is only for the product functionality and not for help in deploying 
# or using the template or script itself. 

import shutil
import requests
import os
from pathlib import Path

url = 'https://raw.githubusercontent.com/0xSteady/minionsparser.py/main/minionsparser.py'
response = requests.get(url)

output = open("/usr/src/app/minionsparser.py", "w")
output.writelines(response.text)

print('The file was saved successfully')

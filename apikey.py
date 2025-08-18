# Author: Tekola
# Date: March 19, 2024
# Version: 1

import sys
import json
import requests
import getpass
import panos
import urllib3
from panos import panorama, firewall, network, objects
import ast

# API account without Commit privilege should be created on the device
# API account name used here is -- ******** --
# API account password = PASSWORD = "************"
# For the https cert validation, add/append the Root/Intermediate(s) of the site into the location
# .../lib/python3.9/site-packages/certifi/cacert.pem
#

PASSWORD = getpass.getpass()
# url for each device that the key is generated
url = "https://<URL>"
# Replace URL with the IP or FQDN of the device

# refer RestAPI documentation https://<url>/restapi-doc

url_plus_parameters = url+"/api/?type=keygen&user=devops&password="+PASSWORD
response = requests.get(url_plus_parameters, verify=True)
print()

APIKEY = response.text.split("<key>")[1].split("</key>")[0]

print(APIKEY)
print()
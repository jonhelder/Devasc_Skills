#!/usr/bin/env python
# Filename: restconf-POST.py
import requests
import json

# Suppress HTTPS warnings
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Print a stream of bytes as pretty JSON
def printBytesAsJSON(bytes):
	print(json.dumps(json.loads(bytes), indent=2))

payload = """
          {
                "severity": "alerts"
          }
"""

# Retrieve configuration through RESTCONF
response = requests.post(
	url = "https://192.168.56.102/restconf/data/Cisco-IOS-XE-native:native/logging/monitor",
	auth = ("cisco", "cisco123!"),
	headers = {
		"Accept": "application/yang-data+json",
                "Content-Type": "application/yang-data+json"
	},
        data = payload,
	verify = False)

#het antwoord schijnt in de headers te staan en komt met enkele qoutes; json wil dubbele!!
antwoord = str(response.headers)
antwoord = antwoord.replace("\'", "\"")

print(response)
# Pretty print our JSON response
printBytesAsJSON(antwoord)


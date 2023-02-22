import requests
import json
import time

while(True):
  url = "https://api.cloudflare.com/client/v4/zones/<zone-id>/dns_records/<record-ip>"
  getip = requests.get("https://api.ipify.org").text
  payload = json.dumps({
    "type": "A",
    "comment": "auto update",
    "content": getip,
    "name": "<dns-name>",
    "proxied": False,
    "ttl": 1
  })
  headers = {
    'X-Auth-Key': '<apikey>',
    'Content-Type': 'application/json',
    'X-Auth-Email': '<email>',
  }
  response = requests.request("PUT", url, headers=headers, data=payload)
  print(response.text)
  time.sleep(300)

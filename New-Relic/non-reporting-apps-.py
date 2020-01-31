#!/usr/bin/env python

import requests
import json
import sys
import os

nr_url = "https://api.newrelic.com/v2/applications.json"

res = requests.get(nr_url, headers={"X-Api-Key":"New-Relic-Account-API-Key"})
app_json = json.loads(res.content)

i = 0
for task in app_json["applications"][:-1]:
    if task["reporting"] == 0:
            print task["name"], task["id"]
    i += 1

#!/usr/bin/env python3
import json


config_file = 'configuration/configuration.json'
with open(config_file) as data_file:
  config = json.load(data_file)

import json
from pprint import pprint

with open('config.json') as config_file:
    data = json.load(config_file)

dynamodb_endpoint = data['dynamodb']['endpoint']
dynamodb_region = data['dynamodb']['region']
dynamodb_table = data['dynamodb']['table']
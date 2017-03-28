
import json
import pprint
import requests
import sys
import simplejson as json


archivo = sys.argv[1]
ip = sys.argv[2]
puerto = sys.argv[3]
idelastic = sys.argv[4]

url = 'http://localhost:9200/israel/israel/1"



json_data=open(archivo)
data = json.load(json_data)
json_data.close():

#print "Dimension: ", data['cubes'][cube]['dim']
#print "Measures:  ", data['cubes'][cube]['meas']
headers = {'Content-type': 'application/json'}
r = requests.post(url, data=json.dumps(data), headers=headers)


import json
from pprint import pprint
import requests
import sys
import simplejson as json

url = 'http://127.0.0.1:8081'



archivo = sys.argv[1]

json_data=open(archivo)
data = json.load(json_data)
json_data.close()

#print "Dimension: ", data['cubes'][cube]['dim']
#print "Measures:  ", data['cubes'][cube]['meas']
headers = {'Content-type': 'application/json'}
r = requests.post(url, data=json.dumps(data), headers=headers)


import json
import pprint
import requests
import sys
import simplejson as json


archivo = sys.argv[1]
#ip = sys.argv[2]
#puerto = sys.argv[3]
#idelastic = sys.argv[4]

url = 'http://10.110.70.148/graduates/quiz1/?pretty'



json_data=open(archivo)
data = json.load(json_data)
json_data.close()


headers = {'Content-type': 'application/json'}
r = requests.post(url, data=json.dumps(data), headers=headers)
print(r.text)
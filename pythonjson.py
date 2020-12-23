import json
onerow = '{ "id" : "01002", "city" : "CUSHMAN", "loc" : [ -72.51564999999999, 42.377017 ], "pop" : 36963, "state" : "MA" }'
dataonerow = json.loads(onerow)
print ("printing one row")
print(dataonerow)

print('Loading from a single value JSON File Now')
with open('zipssingle.json') as f:
  singledata = json.load(f)

print(singledata)

datalist = []
print("Loading from a JSON File Now")
with open('zips.json') as f:
  for jsonObj in f:
    data = json.loads(jsonObj)
    datalist.append(data)

zips_jsondump = json.dumps(datalist)
print(zips_jsondump)
"""
#works but code above prints it into JSON format
print("Let us print the JSON file now")
for dataitem in datalist:
    print(dataitem["id"],dataitem["city"],dataitem["loc"],dataitem["pop"],dataitem["state"])
"""


##{ "id" : "01001", "city" : "AGAWAM", "loc" : [ -72.622739, 42.070206 ], "pop" : 15338, "state" : "MA" }
##{ "id" : "01002", "city" : "CUSHMAN", "loc" : [ -72.51564999999999, 42.377017 ], "pop" : 36963, "state" : "MA" }
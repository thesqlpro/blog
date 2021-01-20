from azure.cosmos import exceptions, CosmosClient, PartitionKey
import json
from easydict import EasyDict as edict
import connecttocosmos as c2c


database = c2c.database
container = c2c.container


query = "SELECT * FROM c"
items = list(container.query_items(
    query=query,
    enable_cross_partition_query=True
))

request_charge = container.client_connection.last_response_headers['x-ms-request-charge']

print('Query returned {0} items. Operation consumed {1} request units'.format(len(items), request_charge))


print ('Loading Zips file to Database')
datalist = []
with open('zips.json') as f:
  for jsonObj in f:
    data = json.loads(jsonObj)
    datalist.append(data)

##print ('printing data list')
##print (datalist)

zips_jsondump = json.dumps(datalist)
##print(zips_jsondump)

##these counters are designed to count RUs for all the inserts
insert_request_counter=0
insert_request=0


print("Let's upload the JSON file to Cosmos now")
for i in datalist:
    ##print(i)
    container.create_item(body=i)
    insert_request = float(container.client_connection.last_response_headers['x-ms-request-charge'])
    insert_request_counter = insert_request_counter + insert_request
   ## print(dataitem["id"],dataitem["city"],dataitem["loc"],dataitem["pop"],dataitem["state"])
   ## json_data =  edict('id':dataitem.[0], 'city' : dataitem.city, 'loc' : dataitem.loc, 'pop' : dataitem.pop, 'state': dataitem.state})
      ##  {dataitem["id"],dataitem["city"],dataitem["loc"],dataitem["pop"],dataitem["state"]})
    ##container.create_item(body=json_data)

print("Total RU Requests")
print(insert_request_counter)
##Final query
countquery = "SELECT value count(1) FROM c"
items = list(container.query_items(
    query=countquery,
    enable_cross_partition_query=True
))

print("Total number of documents in collection")
print(container.query_items(
        query= countquery,
        enable_cross_partition_query=True))

request_charge = container.client_connection.last_response_headers['x-ms-request-charge']

print('Query returned {0} items. Operation consumed {1} request units'.format(len(items), request_charge))




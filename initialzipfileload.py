from azure.cosmos import exceptions, CosmosClient, PartitionKey
import json
from easydict import EasyDict as edict

# Initialize the Cosmos client
endpoint = "https://aymancosmos.documents.azure.com:443/"
key = 'wwHJYw8GUy3078ZDjoUWOd28qrkVUIX2DDbPhVFUESnVEgCbTTGNPZFWLVqVTu9jrAlMjUDklkulUgzUZ5bafg=='

# <create_cosmos_client>
client = CosmosClient(endpoint, key)
# </create_cosmos_client>

# Create a database
# <create_database_if_not_exists>
##database_name = 'AzureSampleFamilyDatabase'
database_name = 'zipsdb'
database = client.create_database_if_not_exists(id=database_name)
# </create_database_if_not_exists>

# Create a container
# Using a good partition key improves the performance of database operations.
# <create_container_if_not_exists>
container_name = 'zipcodes'
container = database.create_container_if_not_exists(
    id=container_name, 
    partition_key=PartitionKey(path="/state"),
    offer_throughput=400
)
# </create_container_if_not_exists>

query = "SELECT * FROM c"
items = list(container.query_items(
    query=query,
    enable_cross_partition_query=True
))

request_charge = container.client_connection.last_response_headers['x-ms-request-charge']

print('Query returned {0} items. Operation consumed {1} request units'.format(len(items), request_charge))


print ('Loading Zips file to Python Object')
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


print(insert_request_counter)
##Final query
query = "SELECT value count(1) FROM c"
items = list(container.query_items(
    query=query,
    enable_cross_partition_query=True
))

print(container.query_items(
        query='SELECT value count(1) FROM c',
        enable_cross_partition_query=True))

request_charge = container.client_connection.last_response_headers['x-ms-request-charge']

print('Query returned {0} items. Operation consumed {1} request units'.format(len(items), request_charge))




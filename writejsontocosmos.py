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
database_name = 'testjsonpython'
database = client.create_database_if_not_exists(id=database_name)
# </create_database_if_not_exists>

# Create a container
# Using a good partition key improves the performance of database operations.
# <create_container_if_not_exists>
container_name = 'zipcodes'
container = database.create_container_if_not_exists(
    id=container_name, 
    partition_key=PartitionKey(path="/id"),
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


datalist = []
with open('zips.json') as f:
  for jsonObj in f:
    data = json.loads(jsonObj)
    datalist.append(data)

"""
print("Loading from a JSON File Now")
with open('zips.json') as f:
  for jsonObj in f:
    data = json.loads(jsonObj)
    datalist.append(data)

zips_jsondump = json.dumps(datalist)
##print(zips_jsondump)
"""
print ('printing data list')
##print (datalist)

zips_jsondump = json.dumps(datalist)
##print(zips_jsondump)
print("Let's upload the JSON file to Cosmos now")
for i in datalist:
    ##print(i)
    container.create_item(body=i)
   ## print(dataitem["id"],dataitem["city"],dataitem["loc"],dataitem["pop"],dataitem["state"])
   ## json_data =  edict('id':dataitem.[0], 'city' : dataitem.city, 'loc' : dataitem.loc, 'pop' : dataitem.pop, 'state': dataitem.state})
      ##  {dataitem["id"],dataitem["city"],dataitem["loc"],dataitem["pop"],dataitem["state"]})
    ##container.create_item(body=json_data)


##Final query
query = "SELECT * FROM c where c.city ='Laurel'"
items = list(container.query_items(
    query=query,
    enable_cross_partition_query=True
))

request_charge = container.client_connection.last_response_headers['x-ms-request-charge']

print('Query returned {0} items. Operation consumed {1} request units'.format(len(items), request_charge))


""""sample code
# Iterating over fake person data and storing in DB
for i in range(50):
    json_data = edict({'first_name': fake.first_name(),
                       'last_name': fake.last_name(),
                       'age': random.randint(30, 50),
                       'address': {'city': fake.city(),
                                   'state': fake.state()}})
    client.CreateItem(container['_self'], json_data)
    """""



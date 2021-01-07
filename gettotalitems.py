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

##SELECT TOP 4 COUNT(1) AS foodGroupCount, f.foodGroup
##FROM Food f
##GROUP BY f.foodGroup

query = "select value count(1) from c"
items = list(container.query_items(
    query=query,
    enable_cross_partition_query=True
))

print(query)
request_charge = container.client_connection.last_response_headers['x-ms-request-charge']
print('Query returned {0} items. Operation consumed {1} request units'.format(len(items), request_charge))
print (items)

statename = 'MD'
##query2 = "select c.id, c.state from zipcodes c where c.state = 'MD'"
query2 = "select value count(1) from zipcodes c where c.state = '" +statename + "'"
##query2 = "select top 4 count(1) as stateCount, c.state from zipcodes c group by c.state"
items2 = list(container.query_items(
    query=query2,
    enable_cross_partition_query=True
))

print(query2)
request_charge = container.client_connection.last_response_headers['x-ms-request-charge']
print('Query returned {0} items. Operation consumed {1} request units'.format(len(items2), request_charge))
print (statename)
print (items2)


print("Get count of records by state without Group By")
stateslistquery = "Select distinct c.state from c"
stateslist = list(container.query_items(
    query = stateslistquery, 
    enable_cross_partition_query = True))

##query3 = "select value count(1) from zipcodes c where c.state = '" +statename + "'"
print (stateslist)
'''
for i in stateslist:
    print(
        list(container.query_items(
        query = "select value count(1) from zipcodes c where c.state = @state",
        parameters = [dict(name = "@state", value=i.values())],
        enable_cross_partition_query = True
    ))
    )
    print(i.values())
 '''   

for i in stateslist:
    statequerycount = "select value count(1) from zipcodes c where c.state = '" + str(i.values()) + "'"
    print (statequerycount)
    print(
        list(container.query_items(
        query = "select value count(1) from zipcodes c where c.state = @state",
        parameters = [dict(name = "@state", value=str(i.values()))],
        enable_cross_partition_query = True
    ))
    )
    statevalue = list(i.values())
    print(statevalue)
    
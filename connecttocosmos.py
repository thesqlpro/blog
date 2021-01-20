from azure.cosmos import exceptions, CosmosClient, PartitionKey
import json
from easydict import EasyDict as edict
import connectioninfo as ci

# Initialize the Cosmos client
endpoint = ci.endpoint
key = ci.key
database_name = ci.database_name
container_name = ci.container_name
client = CosmosClient(endpoint, key)

print("Database Name: " + database_name)
database = client.create_database_if_not_exists(id=database_name)

print("Container Name: " + container_name)
container = database.create_container_if_not_exists(
    id=container_name, 
    partition_key=PartitionKey(path="/id"),
    offer_throughput=400
)


from azure.cosmos import exceptions, CosmosClient, PartitionKey
import json
import pythonjson


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
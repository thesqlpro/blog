from azure.cosmos import exceptions, CosmosClient, PartitionKey
import family

# Initialize the Cosmos client
endpoint = "https://aymancosmos.documents.azure.com:443/"
key = 'wwHJYw8GUy3078ZDjoUWOd28qrkVUIX2DDbPhVFUESnVEgCbTTGNPZFWLVqVTu9jrAlMjUDklkulUgzUZ5bafg=='

# <create_cosmos_client>
client = CosmosClient(endpoint, key)
# </create_cosmos_client>

# Create a database
# <create_database_if_not_exists>
##database_name = 'AzureSampleFamilyDatabase'
database_name = 'aymancosmosdb'
database = client.create_database_if_not_exists(id=database_name)
# </create_database_if_not_exists>

# Create a container
# Using a good partition key improves the performance of database operations.
# <create_container_if_not_exists>
container_name = 'zipcodes'
container = database.create_container_if_not_exists(
    id=container_name, 
    partition_key=PartitionKey(path="/lastName"),
    offer_throughput=400
)
# </create_container_if_not_exists>

query = "SELECT * FROM c"## WHERE c.lastName IN ('Wakefield', 'Andersen')"

items = list(container.query_items(
    query=query,
    enable_cross_partition_query=True
))

request_charge = container.client_connection.last_response_headers['x-ms-request-charge']

print('Query returned {0} items. Operation consumed {1} request units'.format(len(items), request_charge))
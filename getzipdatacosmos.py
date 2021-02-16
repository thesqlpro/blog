from azure.cosmos import exceptions, CosmosClient, PartitionKey
import connecttocosmos as c2c

database = c2c.database
container = c2c.container

##Final query
query = "SELECT * FROM c where c.state ='VA'"
items = list(container.query_items(
    query=query,
    enable_cross_partition_query=True
))

request_charge = container.client_connection.last_response_headers['x-ms-request-charge']
print(query)
print('Query returned {0} items. Operation consumed {1} request units'.format(len(items), request_charge))

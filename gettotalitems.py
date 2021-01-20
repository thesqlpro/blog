from azure.cosmos import exceptions, CosmosClient, PartitionKey
import json
from easydict import EasyDict as edict
import connecttocosmos as c2c

database = c2c.database
container = c2c.container

query = "select value count(1) from c"
items = list(container.query_items(
    query=query,
    enable_cross_partition_query=True
))

print(query)
request_charge = container.client_connection.last_response_headers['x-ms-request-charge']
print('Query returned {0} items. Operation consumed {1} request units' .format(items, request_charge))
##print (items)

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
print('Query returned {0} items. Operation consumed {1} request units'.format(items2, request_charge))
##print (statename)
##print (items2)


print("Get list of states")
stateslistquery = "Select distinct c.state from c"
stateslist = list(container.query_items(
    query = stateslistquery, 
    enable_cross_partition_query = True))

request_charge = container.client_connection.last_response_headers['x-ms-request-charge']
print('Query returned {0} items. Operation consumed {1} request units'.format(len(stateslist), request_charge))
##query3 = "select value count(1) from zipcodes c where c.state = '" +statename + "'"
##print (stateslist)

print("Get count of records by state without Group By")
for i in stateslist:
    statequerycount = "select value count(1) from zipcodes c where c.state = '" + i['state'] + "'"
    print (statequerycount)
    countperstate = (
        list(container.query_items(
        query = statequerycount,
        parameters = [dict(name = "@state", value=str(i.values()))],
        enable_cross_partition_query = True
    ))
    )
    ##statevalue = list(i.values())
    ##totalstatecount = totalstatecount + statevalue
    ##print(statevalue)
    print(countperstate)
    request_charge = container.client_connection.last_response_headers['x-ms-request-charge']
    print('Query returned {0} items. Operation consumed {1} request units'.format(countperstate, request_charge))

'''
###version2
for i in stateslist:
    statequerycount = "select value count(1) from zipcodes c where c.state = '" + i['state'] + "'"
    print (statequerycount)
    state_counts = (
        list(container.query_items(
        query = statequerycount,
        parameters = [dict(name = "@state", value=str(i.values()))],
        enable_cross_partition_query = True
    ))
    )
    print(state_counts[0])
    '''

    
import connecttocosmos


string = "{'state': 'LA'}"
print(string[0:5])

stateslistquery = "Select distinct c.state from c"
stateslist = list(connecttocosmos.container.query_items(
    query = stateslistquery, 
    enable_cross_partition_query = True))

print(stateslist)

print(stateslist.values())
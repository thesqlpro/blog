import connecttocosmos as c2c

container1 = c2c.container

string = "{'state': 'LA'}"
print(string[0:5])

stateslistquery = "Select distinct c.state from c"
stateslist = list(container1.query_items(
    query = stateslistquery, 
    enable_cross_partition_query = True))

print(stateslist)

##print(stateslist.values())

##ignore
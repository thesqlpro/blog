# cosmosdbproject

Create a file called connectioninfo.py 
File needs to look like this:

endpoint = "https://YourCosmosDBName.documents.azure.com:443/"

key = 'YourConnectionKeyValue'

database_name ="DatabaseName"

container_name = "ContainerName"

For local emulator use the following:

endpoint = "https://localhost:8081"

key is available on the mananagement portal

https://localhost:8081/_explorer/index.html


For emulator on a container use

endpoint = "https://IPADDRESSFORCONTAINERHOST:8081"

key is available on the management portal

https://IPADDRESSFORCONTAINERHOST:8081/_explorer/index.html

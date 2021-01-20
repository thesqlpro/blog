##This program is designed to create a new database collection and load it with the zip codes
##after that, we'll run some queries to test.
##It basically calls other python scripts
import connecttocosmos
import sys
import datetime

##Initial load based on if the parameter passed is Y otherwise this is skipped
print(datetime.datetime.now())
initialload = sys.argv[1]
if initialload == 'Y':
    print("Running initial data load")
    exec(open("initialzipfileload.py").read())
else:
    print("Skipping initial data load")


exec(open("getzipdatacosmos.py").read())
exec(open("gettotalitems.py").read())
print(datetime.datetime.now())

#!/usr/bin/python3
import jsondb
import datetime

#changing API key to "example"
jsondb.apikey("example")

#get the key "test_key"
out = jsondb.storeValue("test-time", str(datetime.datetime.now()))

#printing the result
if out:
    print("Stored value "+str(datetime.datetime.now()))
else:
    print("Error while storing value "+str(datetime.datetime.now()))
#!/usr/bin/python3
import jsondb

#changing API key to "example"
jsondb.apikey("example")

#get the key "test_key"
get = jsondb.getValue("test_key")

#printing the result
print("Test key: "+get)
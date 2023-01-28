# <img src="https://github.com/Nicrom098195/JsonDB/blob/main/JsonDB.png?raw=true" alt="Logo" width="23px"/>Json DB<img src="https://github.com/Nicrom098195/JsonDB/blob/main/JsonDB.png?raw=true" alt="Logo" width="23px"/>
## An open-source DB written in Php and Json


JsonDB is a simple DataBase system written in php and json, that can store online data and recover them in any programming language.

## Getting an API key

To use JsonDB you can use the **demo_key** api key, but everyone can read the data in the **demo_key** DataBase.

You can get your own API key at [this link](https://jsondb.nicrom09.repl.co/), and use it.
You can generate multiple API keys, and use them in different applications, or all in one big application.

## Using Python library

Unfortunately, I have tried to upload on pypi, but it gives me so many errors.
To install, you must to put the file in [src/jsondb.py](https://github.com/Nicrom098195/JsonDB/blob/main/src/jsondb.py) in the main directory of your project.

After installation, you can easy get datas from your JsonDB in python, with only three lines of code:

##### To store data:

    import jsondb
    
    jsondb.apikey("demo_key")
    jsondb.storeValue("Tag", "Value")

##### To get data:

    import jsondb 

    jsondb.apikey("demo_key")
    value = jsondb.geValue("Tag")


##### To get all the db:

    import jsondb

    jsondb.apikey("demo_key")
    db = jsondb.getDb()

## Using other languages

You can access to *JsonDB* in any language, and we are working to a GUI for manage it.

To access JsonDB you must to make an HTTP request to some URLs

##### To store a value:

    https://jsondb.nicrom09.repl.co/manage.php?action=store&api_key=demo_key&tag=Tag&value=Value

##### To get a value

    https://jsondb.nicrom09.repl.co/manage.php?action=get&api_key=demo_key&tag=Tag

##### To get all the db

    https://jsondb.nicrom09.repl.co/manage.php?action=getdb&api_key=demo_key

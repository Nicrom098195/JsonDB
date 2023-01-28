import requests

apikey="demo_key"

def apikey(key):
    global apikey
    apikey = key

def getValue(tag):
    res = requests.get("https://jsondb.nicrom09.repl.co/manage.php?action=get&api_key="+apikey+"&tag="+tag)
    return res.text

def storeValue(tag, value):
    res = requests.get("https://jsondb.nicrom09.repl.co/manage.php?action=store&api_key="+apikey+"&tag="+tag+"&value="+value)
    if str(res.text) == "1":
        return True
    else:
        return False

# 1-2 small programs

## for

``` py
# ex 1-1
for loop in 1, "str" :
    print(loop)
```

## list

* list : order (o) array(o) : only string 
* set : order (x) array(o)

``` py
# ex 1-2
list = ["~", "~"]
```

## dictionary 

like hashmap, hashtable

``` py
# ex 1-3
dict = {
    "a" : "~" ,
    "b" : "~" 
    }
str = "a"
print(dict[str])
```

# 1-3 bigger programs

## library modules

``` py
# ex 1-4
import webbrowser
import json
# from library import function
from urllib.request import urlopen

site = input("Type a website URL: ")
era = input("Type a year, month, and day, like 20150613: ")
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)
response = urlopen(url)
text = response.read().decode("utf-8")
data = json.loads(text)
# {'url': 'lolcats.com', 'timestamp': '20150613', 'archived_snapshots': {'closest': {'available': True, 'url': 'http://web.archive.org/web/20150610081618/http://www.lolcats.com/', 'timestamp': '20150610081618', 'status': '200'}}}
try:
    # extract its value from a three-level Python dictionary.
    old_site = data["archived_snapshots"]["closest"]["url"]
    webbrowser.open(old_site)
except:
    print("Sorry, no luck finding", site)
```

# 1-5 Why Python

* simple and compact
* google-selected
* Data Science and Machine Learning

# 1-6 Disadvs

* Static: C/C++, Java, Rust, Go
* Dynamic(script): Python PHP

=> low speed</br>
but its std interpreter is by C -> developing now

## Popularity

# 1-11 The Zen of Python

by Tim Peters 

* Beautiful is better than ugly.
* Simple is better than complex. 
* Complex is better than complicated. 
* Readability counts. 

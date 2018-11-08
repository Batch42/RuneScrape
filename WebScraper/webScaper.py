from requests import get
import json
import time
#retrieves json from specified url

itemDict = {}

text = open("./items", "r").read()
text = text.split("\n")[:-1]
url = 'http://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item='

def get_item(url):
    text = get(url)
    print(text.text)
    patience = 1
    while(True):
      if text.text is '':
        print(url)
        patience *= 2
        time.sleep(patience)
      else:
        patience = 1
        j=text.json()
        print(j['item']['name'])
        break;
      #print(j['item']['today'])
    

for names in text:
  names = names.split(":")
  itemDict[names[1]] = names[0]

for items in itemDict:
  newrl = url + itemDict[items]
  get_item(newrl)
  time.sleep(1)
  


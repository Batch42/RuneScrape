from requests import get
import json
import time
#retrieves json from specified url

itemDict = {}

text = open("./items", "r").read()
text = text.split("\n")[:-1]
f = open("Day1.txt", "a")
url = 'http://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item='

def get_item(url):
    text = get(url)
    patience = 5
    #print(text.text)
    while(True):
        if text.text is '':
            print("WAITING")
            time.sleep(patience)
            text = get(url)
        else:
            patience = 5
            j=text.json()
            name = j['item']['name']
            base_price = j['item']['current']['price']
            today_price = j['item']['today']['price']
            past_price = j['item']['day30']['change']
            print(name)
            #print(base_price)
            #print(today_price)
            #print(past_price)
            f.write(name + "\n" + str(base_price) + "\n" + str(today_price) + "\n" + str(past_price) + "\n")
            break;

for names in text:
  names = names.split(":")
  itemDict[names[1]] = names[0]

for items in itemDict:
  newrl = url + itemDict[items]
  get_item(newrl)
time.sleep(5)

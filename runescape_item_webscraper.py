from requests import get
import json

#retrieves json from specified url
def get_item():
    url = 'http://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item=4151'
    text = get(url)
    j=text.json()
    print(j['item']['today'])

get_item()

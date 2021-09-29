from bs4 import BeautifulSoup
import re
from pprint import pprint
# soup = BeautifulSoup("https://www.worldometers.info/geography/how-many-countries-in-asia/",'html.parser')

# pprint(soup)

import requests
val = requests.get("https://www.worldometers.info/geography/how-many-countries-in-asia/")
data = val.text
jlinks = val.text.html.xpath('//a/@href')
pprint(jlinks)

# for x in data:
#     print(x)
#     if re.search('/world-population/',x):
#         print(x)


from bs4 import BeautifulSoup
import datetime
from dateutil import parser
import requests
import json

url = 'https://myaccount.stockport.gov.uk/bin-collections/show/100011458255'
page = requests.get(url)

if page.status_code != 200:
    exit(1)

soup = BeautifulSoup(page.text, 'html.parser')

out = {}
bh3s = soup.find_all('td', class_="service-name")
bpds = soup.find_all('td', class_="next-service")

for i in range(len(bpds)):
    bin_colour = str(bh3s[i].contents[3]).lower().split('>')[1].split(' ')[0]
    out[bin_colour] = parser.parse(bpds[i].contents[2].lstrip().split(',')[0]).strftime('%Y-%m-%d')

print(json.dumps(out))


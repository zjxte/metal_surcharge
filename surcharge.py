import random
import requests
from lxml import etree
import time
import csv

def get_info(month):
    url = "https://secure.outokumpu.com/das/aaf/openReport3.aspx?format=tab&type=MAS&prodType=0&mode=default&lang=EN&cult=sv-SE&xz=0.cba9b1624e6e3&aafPeriod=" + year + month
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }
    r = requests.get(url=url, headers=headers)
    tree = etree.HTML(r.text)
    surcharge = {}
    month = tree.xpath('//tr[2]/td/text()')[0].replace("Monthly Alloy Surcharges\r\n ", "")
    update_date = tree.xpath('//tr[3]/td[3]/text()')[0].replace("Updated:", "")
    l304 = tree.xpath('//tr[16]/td[5]/text()')[0]
    l316 = tree.xpath('//tr[22]/td[5]/text()')[0]
    s2205 = tree.xpath('//tr[29]/td[5]/text()')[0]
    a825 = tree.xpath('//tr[31]/td[5]/text()')[0]
    surcharge = {
        "Monthly Alloy Surcharge (£) " : month,
        "Updated" : update_date,
        "304L" : int(l304),
        "316L" : int(l316),
        "S2205" : int(s2205),
        "A825" : int(a825)
    }
    # print(surcharge)
    time.sleep(random.randint(1,3))
    return surcharge

year = "2022"

if year == "2022":
    months = ['01','02','03','04','05','06','07','08']
else:
    months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

for month in months:
    data = get_info(month)
    print(data)


import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from requests_ip_rotator import ApiGateway, EXTRA_REGIONS, ALL_REGIONS
import random

key_id = 'AKIARSU7K3JQWVPOZV72'
secret_key = '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'

cookies = {
    'session-id': '258-5965937-1481739',
    'session-id-time': '2082787201l',
    'i18n-prefs': 'INR',
    'ubid-acbin': '262-9353634-4686744',
    'session-token': 'LkNzzq+EbJ1DBY9a422qj/Nj51jhUkvavH+WeGlHA9esFkV7jBg8meaewFfohOCIQlRH015Up/bMNJNiH5RDDZHsn3JzNWf2d8EF8CPDCs64uglTEN+WzYIVCFePEBxYWuszo//2ORnWB90Mf6vwt5AwexTyyzuAEfMw6+h7g/5VeJ9Vf4n2AOOArPVfWEo0/X32T/I0J5FsY1QY64xyY1Am6gnpLp2E59cyantZtxN/FBb5f9TmFhWMhuH78gv1Mg39uNWqkXvEv8EOpjEbClbgsbqkovV9gjrvjjYDUAqvVDft/kiX16VOuOYlAiAtGfcTuVRd6taD8lzsBYqeG6Sc7Js40Cg/',
    'csm-hit': 'tb:s-RCA08544A2YQCT2J63XM|1684211284757&t:1684211285532&adb:adblk_no',

}

def specific_string(length):
    # define the specific string
    sample_string = 'pqrstuvwxyaksdjhkasdlkjqluwoelkansldknc'
    # define the condition for random string
    result = ''.join((random.choice(sample_string)) for x in range(length))
    return result

def trace_id(length):
    # define the specific string
    sample_string = 'pq0rstu1vw2xya3ksdj4hkasdl5kjql6uwo7el8kansl9dknc'
    # define the condition for random string
    result = ''.join((random.choice(sample_string)) for x in range(length))
    
    return result

headers = {
    'User-Agent': specific_string(random.randint(1, 999)),
    'From': specific_string(random.randint(1, 999)),
    'Referer': "https://www.amazon.in/",
}

def scrape_amazon_data():
    url = "https://www.amazon.in/LOMESH-Interlocking-Carpet-Climbing-Bedroom/dp/B0FJ2JGYF4"
    gateway = ApiGateway(url,access_key_id=key_id,access_key_secret=secret_key)
    gateway.start()
    
    session = requests.Session()
    session.mount(url, gateway)
    webpage = session.get(url, headers=headers,cookies=cookies,params={"theme": "light"})
    soup = BeautifulSoup(webpage.text, 'html.parser')
    if webpage.status_code == 200:
        print("Success")
        Derc = soup.find("ul", attrs={"class": 'a-unordered-list a-nostyle a-button-list a-declarative a-button-toggle-group a-vertical a-spacing-top-micro gridAltImageViewLayoutIn1x7'})
        # Derc_src = Derc['src'] if Derc else None
        print(Derc)
    else:
        print(f"Failed to retrieve page. Status Code: {webpage.status_code}")    
   

scrape_amazon_data()
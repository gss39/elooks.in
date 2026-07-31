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

def scrape_amazon_data(x):
    url = f'https://www.amazon.in/s?k=shirts&page={x}'
    gateway = ApiGateway(url,access_key_id=key_id,access_key_secret=secret_key)
    gateway.start()
    
    session = requests.Session()
    session.mount(url, gateway)
    webpage = session.get(url, headers=headers,cookies=cookies,params={"theme": "light"})
    soup = BeautifulSoup(webpage.text, 'html.parser')
    all_data = []
    if webpage.status_code == 200:
        print("Success")
       
        for data in soup.find_all("div", attrs={"class": 's-product-image-container aok-relative s-text-center s-image-overlay-grey puis-image-overlay-grey s-padding-left-small s-padding-right-small puis-spacing-small s-height-equalized puis puis-v1z7l97026vk2122n5xv1arv4h0'}):
            link =  data.find("a")
            p_link = link.get('href') if link else None

            img =  data.find("img")
            img_src = img['src'] if img else None
        
        for data in soup.find_all("div", attrs={"class": 'a-section a-spacing-small puis-padding-left-micro puis-padding-right-micro'}):
            brand =  data.find("span", attrs={"class": 'a-size-base-plus a-color-base'})
            brand_name = brand.text.strip() if brand else None

            title =  data.find("h2", attrs={"class": 'a-size-base-plus a-spacing-none a-color-base a-text-normal'})
            title_name = title.text.strip() if title else None

            rating =  data.find("span", attrs={"class": 'a-size-small a-color-base'})
            rating_value = rating.text.strip() if rating else None

            reviews =  data.find("span", attrs={"class": 'a-size-mini puis-normal-weight-text s-underline-text'})
            review_count = reviews.text.strip() if reviews else None

            price =  data.find("span", attrs={"class": 'a-price-whole'})
            price_value = price.text.strip() if price else None

            mrp =  data.find("span", attrs={"class": 'a-price a-text-price'})
            mrp_value = mrp.find("span", attrs={"class": 'a-offscreen'})
            my_mrp = mrp_value.text.strip() if mrp_value else None

            discount =  data.find_all("div", attrs={"class": 'a-row'})
            discount_value = discount.find("span")
            my_discount = discount

            all_data.append({"link": p_link, "img_src": img_src, "brand_name": brand_name, "title_name": title_name, "rating_value": rating_value, "review_count": review_count, "price_value":  price_value, "my_mrp":  my_mrp, "my_discount": my_discount  })
            
        


    print(f"Scraped {len(all_data)} items from page {x}.")
    return all_data      

print(scrape_amazon_data(2))

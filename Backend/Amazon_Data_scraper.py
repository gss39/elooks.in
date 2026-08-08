import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import Show_data
from requests_ip_rotator import ApiGateway, EXTRA_REGIONS, ALL_REGIONS
import random
# import pylance



# Essential: Set a browser-like User-Agent to avoid a 503 error
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
#     'Accept-Language': 'en-US, en;q=0.5'
# }


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

cookies = {
    'session-id': '258-5965937-1481739',
    'session-id-time': '2082787201l',
    'i18n-prefs': 'INR',
    'ubid-acbin': '262-9353634-4686744',
    'session-token': 'LkNzzq+EbJ1DBY9a422qj/Nj51jhUkvavH+WeGlHA9esFkV7jBg8meaewFfohOCIQlRH015Up/bMNJNiH5RDDZHsn3JzNWf2d8EF8CPDCs64uglTEN+WzYIVCFePEBxYWuszo//2ORnWB90Mf6vwt5AwexTyyzuAEfMw6+h7g/5VeJ9Vf4n2AOOArPVfWEo0/X32T/I0J5FsY1QY64xyY1Am6gnpLp2E59cyantZtxN/FBb5f9TmFhWMhuH78gv1Mg39uNWqkXvEv8EOpjEbClbgsbqkovV9gjrvjjYDUAqvVDft/kiX16VOuOYlAiAtGfcTuVRd6taD8lzsBYqeG6Sc7Js40Cg/',
    'csm-hit': 'tb:s-RCA08544A2YQCT2J63XM|1684211284757&t:1684211285532&adb:adblk_no',

}

headers = {
    'User-Agent': specific_string(random.randint(1, 999)),
    'From': specific_string(random.randint(1, 999)),
    'Referer': "https://www.amazon.in/",
}

key_id = 'AKIARSU7K3JQWVPOZV72'
secret_key = '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'

file_path = "./Backend/amazon_gadgts.xlsx"
df = pd.read_excel(file_path)


amazon_code = Show_data.return_amazon_code()

def scrape_amazon_data(url):

    gateway = ApiGateway(url,access_key_id=key_id,access_key_secret=secret_key)
    gateway.start()

    session = requests.Session()
    session.mount(url, gateway)
    webpage = session.get(url, headers=headers,cookies=cookies,params={"theme": "light"})
  
    data_list = []

    
    if webpage.status_code == 200:
        # Parse the page content
        soup = BeautifulSoup(webpage.text, 'html.parser')

        item_detals = []
        for div in soup.find_all("div", attrs={"class": 'a-row a-expander-container a-expander-section-container a-section-expander-container'}):
            data = div.find("span", attrs={"class": 'a-expander-prompt'}).text.strip()
            for th in div.find_all("table", attrs={"class": 'a-keyvalue prodDetTable'}):
                th_data = th.text.strip()
                item_detals.append((data, th_data))
                
        else:
            print(f"Failed to retrieve page. Status Code: {webpage.status_code}")

        items_list = []
        for item in item_detals:
            items= re.split(r' {2,}', item[1])
            items_list.append((items))
        # print(f"{items_list[0]}")
        # print(f"{item_detals[0][0]}")   

        th = []
        for item in item_detals:
            th.append(item[0])
        data_th = ",".join(th)
        # print(data_th)
        

        
        td = []
        for i in items_list:
         result_td = "/=/".join(i)
         td.append(result_td)
        data_td = "/*=*/".join(td)
        # print(data_td)

        # print(result_td)

        # listof_items = []
        # for i in range(len(th)):
        #     murze = th[i], td[i]
        #     listof_items.append(murze)

        

        try:
            title = soup.find(id='productTitle').get_text().strip()
        except:
            title = "NILL"
        try:
            Rating = soup.find("span", attrs={"class": 'a-size-small a-color-base'}).text.strip()
        except:
            Rating = "NILL"
        try:     
            Reviews = soup.find("span", attrs={"id": 'acrCustomerReviewText'}).text.strip().replace(')', '').replace('(', '')
        except:
            Reviews = "NILL"     
        try:  
            Discount = soup.find("span", attrs={"class": 'a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage apex-savings-percentage'}).text.strip()
        except:
            Discount = "NILL"
        try:       
            Price = soup.find("span", attrs={"class": 'a-price-whole'}).text.strip().replace('.', '')
        except:
            Price = "NILL"
        try:      
            Mrp = soup.find("span", attrs={"class": 'a-size-small aok-offscreen apex-basisprice-offscreen-label'}).text.strip().replace('₹', '').replace('M.R.P.:', '').replace('.00', '')
        except:
            Mrp = "NILL"
        try:      
            Derc = soup.find("ul", attrs={"class": 'a-unordered-list a-vertical a-spacing-mini'}).text.strip().replace('₹', '').replace('M.R.P.:', '').replace('.00', '')
        except:
            Derc = "NILL"   
        try:      
            p_img = soup.find("img", attrs={"class": 'a-dynamic-image a-stretch-vertical media-block-image-tag'})
            p_img_src = p_img['src']
        except:
            p_img_src = "NILL"     

        all_data_list = [title, Rating, Reviews, Discount, Price, Mrp, Derc, p_img_src]
        data_list.append(all_data_list)
        # print(Mrp)
        # print(all_data_list)
       
    return data_list

def scrape_amazon_data_send():
 total_data_list = []
 for i in amazon_code:
    url = f'https://www.amazon.in/dp/{i[1]}'  # Replace with your actual product URL'
    data = scrape_amazon_data(url)
    list1 = [i[0], i[1]] + data[0]
    total_data_list.append(list1)
    # print(total_data_list)
#  return total_data_list

scrape_amazon_data_send()




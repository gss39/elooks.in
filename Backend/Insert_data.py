import pandas as pd
import mysql.connector
import Amazon_Data_scraper
import Show_data

# 1. Load Excel data
# Replace 'data.xlsx' with your actual file path
# df = pd.read_excel('amazon.xlsx')

# 2. Establish connection to MySQL localhost
conn = mysql.connector.connect(
    host="localhost",
  user="root",
  password="",
  database="goodlooks_database"
)
cursor = conn.cursor()

sql_query = "INSERT INTO `products_data`(`product_code`, `video_code`, `Title`, `Rating`, `Reviews`, `Discount`, `Price`, `Mrp`, `Derc`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"

Scrape_data = Amazon_Data_scraper.scrape_amazon_data_send()
print(Scrape_data)
for i in Scrape_data:
    values = (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]) # Adjust column names as needed
    
    
    cursor.execute(sql_query, values)
    

conn.commit() 
print(f"{cursor.rowcount} Done.")
cursor.close()
conn.close()
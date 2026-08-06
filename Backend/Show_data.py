import mysql.connector

# # 1. Establish the connection
# db_connection = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="goodlooks_database"
# )

# # 2. Create a cursor object
# mycursor = db_connection.cursor()

# mycursor.execute("SELECT * FROM `products_data` WHERE 1 LIMIT 5")

# myresult = mycursor.fetchall()

# def return_amazon_code():
#     amazon_code = []
#     for i in myresult:
#         amazon_code.append(i)
#     # print(amazon_code)    
#     return amazon_code
# return_amazon_code()

import pandas as pd

def return_amazon_code():
    amazon_code = []
    df = pd.read_excel('output.xlsx',skiprows=1,header=None)  
    # Convert the column data into a clean Python list

 
    for index, row in df.iterrows():
        amazon_code.append(row.tolist())
    print(amazon_code)    
    return amazon_code

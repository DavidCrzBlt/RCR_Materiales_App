import mysql.connector
from mysql.connector import Error
#import config
import os

products =[]
ids=[]
prices = []

# DB_NAME = config.DB_NAME
# DB_USERNAME = config.DB_USERNAME
# DB_PASSWORD = config.DB_PASSWORD

DB_NAME = os.environ['DB_NAME']
DB_USERNAME = os.environ['DB_USERNAME']
DB_PASSWORD = os.environ['DB_PASSWORD']

try:
    connection = mysql.connector.connect(host='localhost',
                                         database=DB_NAME,
                                         user=DB_USERNAME,
                                         password=DB_PASSWORD)
    if connection.is_connected():
        db_Info = connection.get_server_info()
        cursor = connection.cursor(buffered=True)
        cursor.execute("SELECT id,product_name,price FROM shop")
        for id,product_name,price in cursor.fetchall():
            ids.append(id)
            products.append(product_name)
            prices.append(price)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()

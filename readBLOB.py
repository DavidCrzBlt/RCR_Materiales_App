import mysql.connector
#import config
import os

# DB_NAME = config.DB_NAME
# DB_USERNAME = config.DB_USERNAME
# DB_PASSWORD = config.DB_PASSWORD

DB_NAME = os.environ['DB_NAME']
DB_USERNAME = os.environ['DB_USERNAME']
DB_PASSWORD = os.environ['DB_PASSWORD']


def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)

def readBLOB(id,photo):

    try:
        connection = mysql.connector.connect(host='localhost',
                                             database=DB_NAME,
                                             user=DB_USERNAME,
                                             password=DB_PASSWORD)

        cursor = connection.cursor()
        sql_fetch_blob_query = "SELECT image FROM shop WHERE id=%s"

        cursor.execute(sql_fetch_blob_query,(id,))
        record = cursor.fetchall()
        for row in record:
            image = row[0]
            write_file(image, photo)

    except mysql.connector.Error as error:
        print("Failed to read BLOB data from MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

#readBLOB(2,"C:\\Users\\david\\Documents\\GitHub\\RCR_Materiales_App\\static\\db_images\\nueva_img.png")




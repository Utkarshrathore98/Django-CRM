import pymysql

dataBase = pymysql.connect(
    host='localhost',
    user='root',
    password='utkarshR@01'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")

import mysql.connector
from dotenv import load_dotenv
load_dotenv()

import os

env_password = os.getenv("DB_PASSWORD")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=env_password,
    database="test"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM students ORDER BY name DESC"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for r in myresult:
    print(r)
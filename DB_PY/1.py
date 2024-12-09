import mysql.connector
#-m pip install mysql-connector-python
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

print(mydb)

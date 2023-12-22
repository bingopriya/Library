import mysql.connector

def connect():
    mydb = mysql.connector.connect(
  host = "localhost:3306",
  user = "root",
  password = "a",
  database = "library"
)

def sadd_book(name, id, author, stock):
  sql = "INSERT INTO book (name, id, author, stock) VALUES ('Maths', '1', 'arun', '93')"

  
# mycursor.execute(sql)
# mydb.commit()
  

  
# # disconnecting from server
# mydb.close()
# print(mydb)
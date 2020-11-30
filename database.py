import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root", # default user="root"
  password="",  # default password=""
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE if not exists fooddb")

mydb = mysql.connector.connect(
  host="localhost",
  user="root", # default user="root"
  password="",  # default password=""
  database="fooddb"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE if not exists starter (dishName VARCHAR(80), dishImg VARCHAR(2048), dishDesc VARCHAR(255), dishPrice int(3))")
mycursor.execute("CREATE TABLE if not exists maincourse	 (dishName VARCHAR(80), dishImg VARCHAR(2048), dishDesc VARCHAR(255), dishPrice int(3))")
mycursor.execute("CREATE TABLE if not exists dessert (dishName VARCHAR(80), dishImg VARCHAR(2048), dishDesc VARCHAR(255), dishPrice int(3))")



# mycursor.execute("INSERT INTO starter VALUES('MANCHURIAN', 'https://cdn.discordapp.com/attachments/779386618838515769/780463046942392330/089.-Veg-Manchurian-500x375.png', 'cuisine dish with Chicken breasts, bell pepper, tomatoes, soy sauce.', 120)")
# mycursor.execute("INSERT INTO starter VALUES('MUSHROOM SOUP', 'https://cdn.discordapp.com/attachments/779386618838515769/780745940121157642/mushroom.jpg', 'dairy-free, tastes amazing and is a mushroom lover’s delight!', 220)")
# mydb.commit()




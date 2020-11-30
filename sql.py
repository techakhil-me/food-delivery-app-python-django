import sqlite3

mycursor = sqlite3.connect('menu.db')

mycursor.execute("CREATE TABLE if not exists starter (dishName VARCHAR(80), dishImg VARCHAR(2048), dishDesc VARCHAR(255), dishPrice int(3))")
mycursor.execute("CREATE TABLE if not exists maincourse	 (dishName VARCHAR(80), dishImg VARCHAR(2048), dishDesc VARCHAR(255), dishPrice int(3))")
mycursor.execute("CREATE TABLE if not exists dessert (dishName VARCHAR(80), dishImg VARCHAR(2048), dishDesc VARCHAR(255), dishPrice int(3))")



mycursor.execute("INSERT INTO starter VALUES('MANCHURIAN', 'https://cdn.discordapp.com/attachments/779386618838515769/780463046942392330/089.-Veg-Manchurian-500x375.png', 'cuisine dish with Chicken breasts, bell pepper, tomatoes, soy sauce.', 120)")
mycursor.execute("INSERT INTO starter VALUES('MUSHROOM SOUP', 'https://cdn.discordapp.com/attachments/779386618838515769/780745940121157642/mushroom.jpg', 'dairy-free, tastes amazing and is a mushroom delight!', 220)")
mycursor.execute("INSERT INTO starter VALUES('PANEER TIKKA', 'https://cdn.discordapp.com/attachments/779386618838515769/782291751301939253/paneer_tikka.png', 'paneer & veggies marinated with yogurt and spices.', 150)")
mycursor.execute("INSERT INTO starter VALUES('CHICKEN LOLLIPOP', 'https://cdn.discordapp.com/attachments/779386618838515769/782291759035449374/chicken_lollipop.png', 'hot and spicy appetizer made whole chicken wings', 200)")

mycursor.execute("INSERT INTO maincourse VALUES('NOODLES', 'https://cdn.discordapp.com/attachments/779386618838515769/783012811012833350/image_11.png', 'spicy and tasty noodles with schezwan sauce', 130)")
mycursor.execute("INSERT INTO maincourse VALUES('FRIED RICE', 'https://thumbs.dreamstime.com/b/chinese-stir-fried-rice-eggs-vegetable-white-plate-white-background-horizontal-photo-chinese-stir-fried-rice-158933918.jpg', 'Indo-Chinese styled rice delicacy', 170)")
mycursor.execute("INSERT INTO maincourse VALUES('BIRYANI', 'https://cdn.discordapp.com/attachments/779386618838515769/782291752156659782/biryani.png', 'fragrant rice layered with tender-spicy chicken', 220)")
mycursor.execute("INSERT INTO maincourse VALUES('NAAN', 'https://cdn.discordapp.com/attachments/779386618838515769/782291749519228928/naan.png', 'soft and chewy naan', 160)")

mycursor.execute("INSERT INTO dessert VALUES('ICE CREAM', 'https://cdn.discordapp.com/attachments/779386618838515769/782291746536161300/icecream.png', 'get your favourite frozen flavour', 100)")
mycursor.execute("INSERT INTO dessert VALUES('RASMALAI', 'https://cdn.discordapp.com/attachments/779386618838515769/782291750853017630/Rasmalai.png', 'delicately flavoured with cardamom and kesar', 105)")
mycursor.execute("INSERT INTO dessert VALUES('GULAB JAMUN', 'https://cdn.discordapp.com/attachments/779386618838515769/782291744439533618/gulab_jamun.png', 'drop, melt in your mouth', 90)")
mycursor.execute("INSERT INTO dessert VALUES('CHOCOLATE CAKE', 'https://cdn.discordapp.com/attachments/779386618838515769/782291756464209930/cake.png', 'moist cake with hot chocolate', 150)")

mycursor.commit()
mycursor.close()
print('this')
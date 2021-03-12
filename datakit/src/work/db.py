import mysql.connector
cnx = mysql.connector.connect(user='caskey5_dannyMorris', password='dsSquad12', host='192.249.124.190',  database='caskey5_buffaloCrime')
mycursor = cnx.cursor()

cnx.close()


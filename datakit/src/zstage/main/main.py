import src.zstage.work.db as db
import mysql.connector
import src.zstage.main.config as config
import pandas as pd
from datetime import datetime

begin_time = datetime.now()
print(begin_time)
config.setConfig("Crime")
cnx = mysql.connector.connect(user='caskey5_dannyMorris', password='dsSquad12', host='192.249.124.190',  database='caskey5_buffaloCrime')
mycursor = cnx.cursor()

file = db.DB().selectStatement("select * from full_incidents")
cnx.close()
type(file)

print(datetime.now()-begin_time)
#table = pd.DataFrame.from_dict(file)
#print(file)
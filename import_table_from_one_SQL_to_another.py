
import sqlite3
import pandas as pd

conn = sqlite3.connect("hist.sqlite")
cursor = conn.cursor()
sql = "SELECT * FROM [Financial in loop]"
table_wanted = pd.read_sql(sql,conn)
print ("Successfully copied table...")
conn.commit()
conn.close()

conn = sqlite3.connect("New_Stk_hist.sqlite")
cursor = conn.cursor()
table_wanted.to_sql(name='Financial in loop', con=conn, index=False, if_exists="replace")
print ("Successfully saved table into new SQL...")
conn.commit()
conn.close()

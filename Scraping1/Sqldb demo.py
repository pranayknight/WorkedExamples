import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()
# CREATE TABLE
c.execute("CREATE TABLE STOCKS(Date text, Trans text, Symbol text, Qty real, Price real)")
# INSERT A ROW OF DATA
c.execute("INSERT INTO STOCKS VALUES ('2006-01-05', 'BUY', 'RHAT', 100, 35.14)")
# SAVE (COMMIT) THE CHANGES
conn.commit()
# WE CAN CLOSE THE CONNECTION IF WE ARE DONE WITH IT
# JUST BE SURE ANY CHANGES HAVE BEEN COMMITED OR ELSE THEY WILL BE LOST
conn.close()

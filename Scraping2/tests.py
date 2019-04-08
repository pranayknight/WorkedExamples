import sqlite3

# Testing the types of data that can be taken by sqlite

conn = sqlite3.connect("Chandimata.db")
cursor = conn.cursor()
jammu = [["Tata", "Chata"],["tamarind","Pastries"],[None,"Kulcha"],[True, False],[456,789]]  # instead of true and false the table took values as 1 and 0
cursor.execute("CREATE TABLE IF NOT EXISTS Tuxedo(trash,dump)")
cursor.executemany("INSERT INTO Tuxedo VALUES(?,?)",jammu)
conn.commit()

cursor.close()
conn.close()

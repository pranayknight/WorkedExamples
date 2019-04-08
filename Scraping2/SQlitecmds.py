import sqlite3

conn = sqlite3.connect("Database_name")
# This query even creates the database in case it doesn't exists

cursor = conn.cursor()
# This query helps us create a cursor for our database and helps us run our queries in a much faster way

# Executing the command through cursor object

cursor.execute("CREATE TABLE Table_Name(col1 Datatype Constarints, col2 Datatype Constraints)")
# This is a simple query to create table in the database

cursor.execute("INSERT INTO Table_Name(col1,col2) VALUES(?,?)", ("a predefined (list or tuple) or even datas directly"))
# Query to insert values in the table one row at a time

cursor.executemany("INSERT INTO Table_Name VALUES(?,?)",("An Array tuple of tuples or lists of lists or manually loads of data"))
# Query to execute many lines at once and insert various rows at a time

cursor.execute("UPDATE Table_Name SET col1='Tinkerbell' WHERE col2=='Bhindi'")
# Query to update table data

cursor.execute("SELECT * FROM Table_Name WHERE col2=='Tamarind'")
result = cursor.fetchall()
print(result)
# Query to fetch data from the table

cursor.execute("Delete from Table_Name")  # To delete entire data from table
cursor.execute("Delete from Table_Name Where Condition")  # To delete specific rows


import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Never do this -- insecure!
symbol = 'RHAT'
c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)
# call the cursor’s fetchone() method to retrieve a single matching row
# or call fetchall() to get a list of the matching rows
print(c.fetchone())

# Do this instead
t = ('RHAT',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t)
print(c.fetchone())

# Larger example that inserts many records at a time
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)


for row in c.execute('SELECT * FROM STOCKS ORDER BY Price'):
    print(row)

conn.close()
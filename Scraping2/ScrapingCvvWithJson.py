import requests
import json
import sqlite3
import pandas as pd


cookies = {
    'csrftoken': 'xeaAIX6s1O13cxAiQe6y3KGFBfMiMbQC',
    'sessionid': 'qe2tr96ucxrwa9bv90eyjrvt7q29etu6',
}

headers = {
    'Origin': 'https://cvv-me.su',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'Content-Type': 'text/plain;charset=UTF-8',
    'Accept': '*/*',
    'Referer': 'https://cvv-me.su/cvv/',
    'Connection': 'keep-alive',
    'X-CSRFToken': 'xeaAIX6s1O13cxAiQe6y3KGFBfMiMbQC',
}

data = '{"offset":0,"type":0}'    # type to be looped to get data from all the pages

response = requests.post('https://cvv-me.su/api/cards/', headers=headers, cookies=cookies, data=data, verify=False)  #cookies and headers need to be updated frequently

conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS CVVdata(Bin, Name, city, Zipcode, State, Price, Bank, Exp, Country)")

freak = response.text
json_decode = json.loads(freak)
full_list = []

lst = json_decode['cards']
# print(lst)
for data in lst:
    onelist = []
    onelist.append(data['bin'])
    onelist.append(data['name'])
    onelist.append(data['city'])
    onelist.append(data['zipcode'])
    onelist.append(data['state'])
    onelist.append(data['price'])
    onelist.append(data['bank'])
    onelist.append(data['exp'])
    onelist.append(data['country'])
    # print(anlist)
    full_list.append(onelist)
    cursor.execute("INSERT INTO CVVdata(Bin,Name,city,zipcode,State,Price,Bank,exp,country) VALUES (?,?,?,?,?,?,?,?,?)", onelist)
    conn.commit()

# or this way  cursor.executemany(""INSERT INTO CVVdata(Bin,Name,city,zipcode,State,Price,Bank,exp,country) VALUES (?,?,?,?,?,?,?,?,?)", full_list)
cursor.close()
conn.close()

# print(fllist)
'''df = pd.DataFrame(full_list, columns=['Bin','Name','City','Zipcode','State','Price','Bank','Exp','Country'])

df.to_csv("triedpg1.csv")'''

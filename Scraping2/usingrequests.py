import json
import requests

cookies = {
    'csrftoken': 'gKm8wydpWPlDm69u0mzBSbAP0nwdTa4N',
    'sessionid': 'qsv05wf0ljfhkot3hg7ga8yb0am60kvj',
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
    'X-CSRFToken': 'gKm8wydpWPlDm69u0mzBSbAP0nwdTa4N',
}

data = '{"offset":1,"type":0}'

response = requests.post('https://cvv-me.su/api/cards/', headers=headers, cookies=cookies, data=data, verify=False)


freak = response.text
print(freak)

print(type(freak))
json_decode = json.loads(freak)
print(type(json_decode))
my_dict = {}
r = open('jsvalue.txt', 'w')
r.write(json_decode)



'''
reqd_data = json_decode['cards']
for item in reqd_data:
    my_dict['bin'] = item.get('bin')
    my_dict['zip'] = item.get('zipcode')

print(my_dict)
'''
'''
json_decode = json.load(freak)
for item in json_decode:
    my_dict = {}
    my_dict['bin'] = item.get('cards').get('bin')
    my_dict['city'] = item.get('cards').get('city')
    my_dict['state'] = item.get('state')

print(my_dict)'''
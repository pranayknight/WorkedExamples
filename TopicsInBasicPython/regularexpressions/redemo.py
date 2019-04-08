import re
str="Take 1 up 1-3-2019 one 23 idea. one idea 45 at a time 12-11-2020"

result=re.search(r'o\w',str)
print(result.group())

result=re.findall(r'o\w\w',str)
print(result)

result=re.match(r'T\w\w',str)   #only looks at the beginning of the string
print(result.group())

result=re.sub(r'one','two',str)
print(result)

result=re.split(r'\d+',str)
print(result)

result=re.findall(r'o\w+',str)
print(result)

result=re.findall(r'o\w*',str)
print(result)

result=re.findall(r'o\w?',str)
print(result)

result=re.findall(r'o\w{1}',str)
print(result)

result=re.findall(r'o\w{2}',str)
print(result)

result=re.findall(r'o\w{1,2}',str)
print(result)

result=re.findall(r'\d{1,2}-\d{1,2}-\d{4}',str)
print(result)

result=re.search(r'^T\w',str)
print(result)

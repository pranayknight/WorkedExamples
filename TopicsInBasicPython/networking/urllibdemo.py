import urllib.request

try:
    url=urllib.request.urlopen("https://www.python.org")
    content=url.read()
    url.close()
except:
    print("The webpage is not found")
    exit()

f=open('python.html','wb')
f.write(content)
f.close()
import requests

r = requests.get("http://www.webscrapingfordatascience.com/basichttp/")

# Which HTTP status code we got back from the server
print(r.status_code)
# What is the textual status code
print(r.reason)
# What were the HTTP response headers
print(r.headers)
# The request information is saved as a Python object in r.request:
print(r.request)
# What were the HTTP request headers
print(r.request.headers)

# The HTTP response content
print(r.text)

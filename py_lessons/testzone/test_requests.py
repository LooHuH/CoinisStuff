import requests as r

response = r.get('https://www.google.com/search?client=firefox-b-d&q=asf', headers=)
print(response.content)
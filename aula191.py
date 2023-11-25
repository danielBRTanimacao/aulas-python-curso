# requests para requisições HTTP
# Tutorial -> https://youtu.be/Qd8JT0bnJGs
import requests

# http:// -> 80
# https:// -> 443

url = 'http://127.0.0.1:5500/aula190_site/index.html'
response = requests.get(url) # resposta

print(response.status_code)
# print(response.headers)
# print(response.content)
print(response.text)
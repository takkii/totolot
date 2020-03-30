import requests

response = requests.get('https://corona-stats.online/Japan')

print(response.text)
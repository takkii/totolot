import requests,re

response = requests.get('https://corona-stats.online/Japan')
pat = re.compile(r"<[^>]*?>")
print(pat.sub("", response.text))

import re
from requests_html import HTMLSession
from bs4 import BeautifulSoup

session = HTMLSession()
response = session.get('https://standb.herokuapp.com')
soup = BeautifulSoup(response.text,"lxml")
[s.decompose() for s in soup('style')]
pat = re.compile(r"<[^>]*?>")
rss_result = (pat.sub("", soup.text))
print(rss_result)

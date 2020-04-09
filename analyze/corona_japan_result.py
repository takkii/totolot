import tkinter as tk, re
from requests_html import HTMLSession
from bs4 import BeautifulSoup

root = tk.Tk()
root.title("Coronavirus Tracker")
root.geometry("800x600")
session = HTMLSession()
response = session.get('https://corona-stats.online/Japan')
soup = BeautifulSoup(response.text,"lxml")
[s.decompose() for s in soup('style')]
pat = re.compile(r"<[^>]*?>")
corona_ja_result = (pat.sub("", soup.text))
#print(corona_ja_result)
tk.Label(root,text=str(corona_ja_result)).pack(fill=tk.X)
root.mainloop()


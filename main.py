import requests
from bs4 import BeautifulSoup

#scraping the website
url = "https://www.setlist.fm/search?artist=53d69b79&query=The+National"
r = requests.get(url)
r.raise_for_status()

html = r.text.encode("utf-8")

# make a soup
soup = BeautifulSoup(html, "html.parser")

#pick out what you want from site
results = soup.find("div", class_="main")
#print(results)
column = results.find("div", class_="rightColumn")
#print(column)
content_box = column.find("div", class_="contentBox")
setlist_preview = content_box.find("div", class_="setlistPreview")
date_block = setlist_preview.find("div", class_="dateBlock")
#print(date_block)
month = date_block.find("span", class_="month")
day = date_block.find("span", class_="day")
year = date_block.find("span", class_="year")

month_text = month.text
day_text = day.text
year_text = year.text

print(f"The National's last show was: {month_text} {day_text}, {year_text}")


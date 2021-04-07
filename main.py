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
#print(content_box)
setlist_preview = content_box.find_all("div", class_="setlistPreview")
#print(len(setlist_preview))
#print(setlist_preview)


#loops through each show setlist on page
for set_list in setlist_preview:
  #pulls out the date
  date_block = set_list.find("div", "dateBlock")
  month = date_block.find("span", class_="month").text
  day = date_block.find("span", class_="day").text
  year = date_block.find("span", class_="year").text

  #pulls out the artist, venue, and location
  title = set_list.find("h2")
  title_text = title.find("a").text
  title_edit = title_text.split(",")
  artist = title_edit[0]
  artist_edit = artist.split(" at ")
  new_artist = artist_edit[0]
  venue = artist_edit[1]
  city = title_edit[1]
  country = title_edit[2]

  print(f"{new_artist} played {venue} in {city}, {country} on {month} {day}, {year}")


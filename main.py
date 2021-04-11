import requests
from bs4 import BeautifulSoup
import math

def get_results(num_results):
  num_of_pages = math.ceil(num_results / 10)
  #print(num_of_pages)

  for num in range(0, num_of_pages):
    #scraping the website
    base_url = "https://www.setlist.fm/"
    search_url = "search?artist=53d69b79&page=" + str(num+1) + "&query=The+National"
    #print(search_url)
    url = base_url + search_url
    #print(url)

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

    #artist_list = []
    #tour_list = []
    #venue_list = []
    #city_list = []
    #state_list = []
    #month_list = []
    #day_list = []
    #year_list = []
    #loops through each show setlist on page
    for setlist in setlist_preview:

      #pulls out the date
      date_block = setlist.find("div", "dateBlock")
      month = date_block.find("span", class_="month").text
      #month_list.append(month)
      day = date_block.find("span", class_="day").text
      #day_list.append(day)
      year = date_block.find("span", class_="year").text
      #year_list.append(year)
      #print(month_list)
      #print(day_list)
      #print(year_list)

      #pulls out the artist, venue, and location
      details = setlist.find("div", "details").text

      details = details.replace("\n", "")
      details = details.split(",")
      #print(details)

      for detail in details:
        detail = detail.strip()
        print(detail)
      print(f"{month} {day}, {year}")
      print("\n")

    #for artist, venue, city, month , day, year in zip(artist_list, venue_list, city_list, month_list, day_list, year_list):
      #print(artist)
      #print(f"Date: {month} {day}, {year}")
      #print(venue)
      #print(f"Location: {city}\n")

      #print(f"{new_artist} played {venue} in {city}, {country} on {month} {day}, {year}")
      #print(f"{title_text} played on {month} {day}, {year}")

get_results(100)



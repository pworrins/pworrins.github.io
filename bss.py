import requests # type: ignore
import json
from bs4 import BeautifulSoup # type: ignore
from datetime import datetime

URL = "https://www.republika.co.id/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

data = []
list_judul = []

for obj in soup.find_all("div", class_="caption"):
    temp_tglTerbit = obj.find("div", class_='date')
    temp_Judul = obj.find("h3")
    if temp_Judul is not None and temp_tglTerbit is not None:
        temp_tglTerbit = temp_tglTerbit.text

        temp_kategori = temp_tglTerbit[0:temp_tglTerbit.find(' -')]
        temp_kategori = temp_kategori.strip()

        temp_tglTerbit = temp_tglTerbit[temp_tglTerbit.find('- ') + 2:]
        temp_tglTerbit = temp_tglTerbit.strip()

        temp_Judul = temp_Judul.find("span")
        temp_Judul_text = temp_Judul.text
        temp_Judul_link = temp_Judul.find_parent("a")["href"]  # Ambil URL dari link judul

        data.append({"judul": temp_Judul_text, "kategori": temp_kategori, "waktu publish": temp_tglTerbit,
                     "waktu scrape": datetime.now().strftime('%a %d %b %Y, %H:%M'), "url": temp_Judul_link})

with open('republika_scraped_data.json', 'w') as f:
    json.dump(data, f, indent=2)

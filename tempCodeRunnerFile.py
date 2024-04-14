import requests  # type: ignore
from bs4 import BeautifulSoup  # type: ignore
import json
from datetime import datetime, timezone

def dptInt(a):
    k = ''
    for i in range(2):
        if a[i] != ' ':
            k += a[i]
    return int(k)

def jamMenit(a):
    if 'menit' in a:
        return True
    else:
        return False

def get_current_time():
    current_time = datetime.now()
    return current_time

def fungsi(waktu):
    if waktu.isdigit():  # Periksa apakah waktu adalah bilangan
        jamAtauMenit = jamMenit(waktu)
        n = int(waktu)
        timestamp = datetime.now().timestamp()
        if jamAtauMenit:
            timestamp -= n * 60
        else:
            timestamp -= n * 3600

        # Convert Unix timestamp to datetime object
        date_time = datetime.fromtimestamp(timestamp, timezone.utc)

        # Format the datetime object as a string
        formatted_date = date_time.strftime('%Y-%m-%d %H:%M:%S')
        return formatted_date
    else:
        # Jika waktu tidak dapat dikonversi menjadi integer, kembalikan waktu asli
        return waktu


def scrape_republika():
    url = 'https://www.republika.co.id/'
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')
    divs = soup.find_all('div', class_='caption')

    dataset = []

    for div in divs:
        subdiv = div.find('div')
        total = []
        try:
            kategoriNwaktu = subdiv.text.strip().split('- ')
            if len(kategoriNwaktu) == 2:
                kategori = kategoriNwaktu[0]
                waktu = kategoriNwaktu[1]
                total.extend((kategori, waktu))
        except AttributeError:
            pass

        subdiv = div.find('h3')
        if subdiv:
            title = subdiv.text.strip()
            #untuk url daro tag<a>
            link = subdiv.find('a')['href']if subdiv.find('a')else ''
            total.append(title)
            total.append(link) 

        if len(total) == 4:
            total[1] = fungsi(total[1])
            dataset.append({'kategori': total[0], 'waktu': total[1], 'judul': total[2],'Link Berita': total[3], 'waktu scraping': str(get_current_time())})

    return dataset

def save_to_json(data):
    with open('republika_scraped_data.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)

def main():
    # Melakukan scraping
    scraped_data = scrape_republika()

    # Menyimpan data ke dalam file JSON
    if scraped_data:
        save_to_json(scraped_data)
        print("Data telah disimpan dalam file JSON.")
    else:
        print("Tidak ada data yang disimpan.")

if __name__ == "__main__":
    main()

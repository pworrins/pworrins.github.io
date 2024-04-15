import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore
import json
from datetime import datetime

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    articles = []
    for item in soup.find_all('li', class_='list-group-item'):
        category_element = item.find('span', class_='kanal-info')
        title_element = item.find('h3')
        date_element = item.find('div', class_='date')

        if category_element and title_element and date_element:
            category = category_element.text.strip()
            title = title_element.text.strip()
            
            # Periksa apakah ada teks pada elemen tanggal
            if date_element.text.strip():
                publish_time = date_element.text.strip().split('-')[-1].strip()
            else:
                publish_time = 'Unknown'
            
            # Ambil link dari judul
            link = item.find('a')['href']
            
            articles.append({
                'judul': title,
                'kategori': category,
                'waktu_publish': publish_time,
                'waktu_scraping': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'url': link  # Tambahkan link ke dalam data artikel
            })
    
    return articles

def save_to_json(data):
   with open('republika_scraped_data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    url = 'https://www.republika.co.id/'
    articles = scrape_website(url)
    print("Selesai scraping")
    save_to_json(articles)
    print("Data disimpan dalam format JSON")

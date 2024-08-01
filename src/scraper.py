import requests
from config.settings import HEADERS, BASE_URL

def fetch_html(url):
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()  
    return response.text

def save_html(html, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(html)

if __name__ == "__main__":
    html = fetch_html(BASE_URL)
    save_html(html, 'data/raw/otodom.html')
    print("HTML saved to data/raw/otodom.html")

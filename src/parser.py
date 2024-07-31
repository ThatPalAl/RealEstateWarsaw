import os
import pandas as pd
from bs4 import BeautifulSoup
import re

def parse_otodom(html_path):
    with open(html_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    listings = []

    for offer in soup.select('div[data-cy="search.listing.organic"] ul.css-rqwdxd.e127mklk0 li'):
        try:
            title = offer.select_one('p[data-cy="listing-item-title"]').text.strip()
            location = offer.select_one('p.css-42r2ms.eejmx80').text.strip()
            price_section = offer.select_one('span.css-2bt9f1.evk7nst0').text.strip()

            rent_price_match = re.match(r'(\d+)\s*zł', price_section)
            admin_fee_match = re.search(r'czynsz:\s*(\d+)\s*zł', price_section)

            rent_price = int(rent_price_match.group(1)) if rent_price_match else 0
            admin_fee = int(admin_fee_match.group(1)) if admin_fee_match else 0

            details = offer.select('div.css-1c1kq07.e1clni9t0 dt ~ dd')
            rooms = details[0].text.strip() if len(details) > 0 else 'N/A'
            size_str = details[1].text.strip() if len(details) > 1 else 'N/A'

            size = float(re.sub(r'\D+', '', size_str))

            listings.append({
                'title': title.replace(',', ' '),
                'location': location.replace(',', ' '),
                'rent_price': rent_price,
                'admin_fee': admin_fee,
                'rooms': rooms.replace(',', ' '),
                'size': size
            })
        except (AttributeError, IndexError, ValueError) as e:
            print(f"Error parsing offer: {e}")
            continue

    return listings

def save_to_csv(listings, csv_path):
    if not listings:
        print("No listings found. Skipping saving to CSV.")
        return
    df = pd.DataFrame(listings)
    df.to_csv(csv_path, mode='w', header=True, index=False)

if __name__ == "__main__":
    html_path = 'data/raw/otodom.html'
    csv_path = 'data/processed/otodom_data.csv'

    listings = parse_otodom(html_path)
    save_to_csv(listings, csv_path)

    print(f"Found {len(listings)} listings.")
    print(f"Data saved to {csv_path}.")

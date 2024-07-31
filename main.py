import os
from src.scraper import fetch_html, save_html
from src.parser import parse_otodom, save_to_csv
from src.data_processor import process_data
from config.settings import BASE_URL

def main():
    html_path = 'data/raw/otodom.html'
    csv_path = 'data/processed/otodom_data.csv'

    # Step 1: Fetch HTML
    print("Fetching HTML...")
    html = fetch_html(BASE_URL)
    save_html(html, html_path)
    print("HTML saved.")

    # Step 2: Parse HTML
    print("Parsing HTML...")
    listings = parse_otodom(html_path)
    print(f"Found {len(listings)} listings.")
    print(f"Parsed data: {listings[:5]}")  # Print first 5 entries for debugging

    # Step 3: Save to CSV
    print(f"Saving {len(listings)} entries to CSV.")
    save_to_csv(listings, csv_path)
    print("Data saved to CSV.")

    # Step 4: Process Data
    print("Processing data...")
    df = process_data(csv_path)
    print(f"Processed DataFrame: \n{df.head()}")

    # Step 5: Launch the GUI application
    os.system("python app.py")

if __name__ == "__main__":
    main()

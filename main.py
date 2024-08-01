import os
import pandas as pd
from src.scraper import fetch_html, save_html
from src.parser import parse_otodom, save_to_csv
from src.data_processor import process_data
from src.past_data_processor import process_past_data
from src.visualization import plot_prices, visualize_listings
from src.map_visualization import plot_map
from config.settings import BASE_URL

def main():
    html_path = 'data/raw/otodom.html'
    csv_path = 'data/processed/otodom_data.csv'
    past_data_path = 'data/processed/data_clean.csv'

    print("Fetching HTML...")
    html = fetch_html(BASE_URL)
    save_html(html, html_path)
    print("HTML saved.")

    print("Parsing HTML...")
    listings = parse_otodom(html_path)
    print(f"Found {len(listings)} listings.")
    print(f"Parsed data: {listings[:5]}") 

    print(f"Saving {len(listings)} entries to CSV.")
    save_to_csv(listings, csv_path)
    print("Data saved to CSV.")

    print("Processing current data...")
    df = process_data(csv_path)
    print(f"Processed DataFrame: \n{df.head()}")

    print("Processing past data...")
    past_df = process_past_data(past_data_path)
    print(f"Processed Past DataFrame: \n{past_df.head()}")

    combined_df = pd.concat([df, past_df], ignore_index=True)
    print(f"Combined DataFrame: \n{combined_df.head()}")

    print("Visualizing data...")
    plot_prices(combined_df)
    visualize_listings(combined_df)
    print("Data visualization complete.")

    print("Creating map...")
    plot_map(combined_df)
    print("Map created.")

if __name__ == "__main__":
    main()

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_prices(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(df['rent_price'], bins=30, kde=True)
    plt.title('Distribution of Rental Prices')
    plt.xlabel('Price (PLN)')
    plt.ylabel('Frequency')
    plt.show()

def display_listings(df):
    for idx, row in df.iterrows():
        print(f"Listing {idx+1}:")
        print(f"Title: {row['title']}")
        print(f"Location: {row['location']}")
        print(f"Rent Price: {row['rent_price']} PLN")
        print(f"Admin Fee: {row['admin_fee']} PLN")
        print(f"Rooms: {row['rooms']}")
        print(f"Size: {row['size']} m²")
        print('-' * 40)

if __name__ == "__main__":
    df = pd.read_csv('data/processed/otodom_data.csv')
    plot_prices(df)
    display_listings(df)

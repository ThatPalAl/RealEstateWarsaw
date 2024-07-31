import pandas as pd

def process_data(filename):
    df = pd.read_csv(filename)
    df['rooms'].fillna('N/A', inplace=True)
    df['title'].fillna('N/A', inplace=True)
    df['location'].fillna('N/A', inplace=True)
    df['rent_price'].fillna(0, inplace=True)
    df['admin_fee'].fillna(0, inplace=True)
    df['size'].fillna(0, inplace=True)

    return df

# Example usage
if __name__ == "__main__":
    df = process_data('data/processed/otodom_data.csv')
    print(df.head())

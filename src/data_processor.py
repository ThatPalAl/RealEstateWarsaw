import pandas as pd

def process_data(filename):
    df = pd.read_csv(filename)
    df['rent_price'] = df['rent_price'].astype(float)
    df['admin_fee'] = df['admin_fee'].astype(float)
    df['size'] = df['size'].astype(float)
    df['rooms'].fillna('N/A', inplace=True)
    df['title'].fillna('N/A', inplace=True)
    df['location'].fillna('N/A', inplace=True)
    df['rent_price'].fillna(0, inplace=True)
    df['admin_fee'].fillna(0, inplace=True)
    df['size'].fillna(0, inplace=True)
    return df

def process_past_data(filename):
    df = pd.read_csv(filename)
    df['rent_price'] = df['rent_price'].astype(float)
    df['admin_fee'] = df['admin_fee'].astype(float)
    df['size'] = df['size'].astype(float)
    return df
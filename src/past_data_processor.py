import pandas as pd

def process_past_data(filename):
    df = pd.read_csv(filename)

    df.rename(columns={
        'gross_price': 'rent_price',
        'area': 'size',
        'room_num': 'rooms',
    }, inplace=True)

    district_columns = df.filter(like='district_').columns
    df['location'] = df[district_columns].apply(lambda x: x.idxmax().replace('district_', ''), axis=1)

    df['title'] = 'N/A'
    df['admin_fee'] = 0
    
    df = df[['title', 'location', 'rent_price', 'admin_fee', 'rooms', 'size']]

    df['rent_price'] = df['rent_price'].astype(float)
    df['admin_fee'] = df['admin_fee'].astype(float)
    df['size'] = df['size'].astype(float)

    df['rooms'] = df['rooms'].astype(str) + ' pokoje'

    return df

if __name__ == "__main__":
    past_data_path = 'data/processed/data_clean.csv'
    past_df = process_past_data(past_data_path)
    print(past_df.head())

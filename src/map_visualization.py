import folium
from geopy.geocoders import Nominatim

def plot_map(df):
    geolocator = Nominatim(user_agent="real-estate-scraper")
    map_osm = folium.Map(location=[52.2297, 21.0122], zoom_start=12)
    
    for _, row in df.iterrows():
        try:
            location = geolocator.geocode(row['location'])
            if location:
                folium.Marker([location.latitude, location.longitude], popup=row['title']).add_to(map_osm)
        except:
            continue
    
    map_osm.save('map.html')

if __name__ == "__main__":
    from data_processor import process_data
    df = process_data('data/processed/otodom_data.csv')
    plot_map(df)

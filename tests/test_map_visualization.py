import pytest
import pandas as pd
from src.map_visualization import plot_map

def test_plot_map():
    sample_data = [
        {'title': 'Sample Title', 'price': 1000, 'location': 'Warszawa'},
        {'title': 'Another Title', 'price': 2500, 'location': 'Kraków'}
    ]
    df = pd.DataFrame(sample_data)
    try:
        plot_map(df)
    except Exception as e:
        pytest.fail(f"plot_map raised an exception: {e}")

if __name__ == "__main__":
    pytest.main()

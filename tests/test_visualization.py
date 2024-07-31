import pytest
import pandas as pd
from src.visualization import plot_prices

def test_plot_prices():
    sample_data = [
        {'title': 'Sample Title', 'price': 1000, 'location': 'Sample Location'},
        {'title': 'Another Title', 'price': 2500, 'location': 'Another Location'}
    ]
    df = pd.DataFrame(sample_data)
    try:
        plot_prices(df)
    except Exception as e:
        pytest.fail(f"plot_prices raised an exception: {e}")

if __name__ == "__main__":
    pytest.main()

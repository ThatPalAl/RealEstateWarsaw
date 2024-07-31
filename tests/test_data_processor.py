import pytest
from src.data_processor import process_data

def test_process_data():
    sample_data = [
        {'title': 'Sample Title', 'price': '1 000 zł', 'location': 'Sample Location'},
        {'title': 'Another Title', 'price': '2 500 zł', 'location': 'Another Location'}
    ]
    df = process_data(sample_data)
    assert not df.empty
    assert 'price' in df.columns
    assert df['price'].dtype == float
    assert df.loc[0, 'price'] == 1000.0
    assert df.loc[1, 'price'] == 2500.0

if __name__ == "__main__":
    pytest.main()

import pytest
from src.parser import parse_html

def test_parse_html():
    sample_html = "<html><body><div class='offer-item-details'><span class='offer-item-title'>Sample Title</span><li class='offer-item-price'>1 000 zł</li><p class='text-nowrap'>Sample Location</p></div></body></html>"
    data = parse_html(sample_html)
    assert len(data) == 1
    assert data[0]['title'] == 'Sample Title'
    assert data[0]['price'] == '1 000 zł'
    assert data[0]['location'] == 'Sample Location'

if __name__ == "__main__":
    pytest.main()

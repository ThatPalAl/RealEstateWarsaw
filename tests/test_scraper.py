import pytest
from src.scraper import fetch_html
from config.settings import BASE_URL

def test_fetch_html():
    html = fetch_html(BASE_URL)
    assert html is not None
    assert '<html' in html

if __name__ == "__main__":
    pytest.main()

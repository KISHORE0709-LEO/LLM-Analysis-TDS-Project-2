import requests
from bs4 import BeautifulSoup

def get_rendered_html(url: str) -> str:
    """Simple web scraper using requests (fallback for when Playwright fails)"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        return response.text
    except Exception as e:
        return f"Error scraping {url}: {str(e)}"
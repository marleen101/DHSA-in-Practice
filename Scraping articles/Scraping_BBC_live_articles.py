import requests
from bs4 import BeautifulSoup
import pandas as pd

# List of live article URLs to scrape
live_urls = [
    "https://www.bbc.co.uk/news/live/world-middle-east-67339462",
    "https://www.bbc.co.uk/news/live/world-middle-east-67504657",
    "https://www.bbc.co.uk/news/live/world-middle-east-67364296",
    "https://www.bbc.co.uk/news/live/world-middle-east-67423274",
    "https://www.bbc.co.uk/news/live/world-middle-east-67324897",
    "https://www.bbc.co.uk/news/live/world-middle-east-67481139",
    "https://www.bbc.co.uk/news/live/world-middle-east-67281166",
    "https://www.bbc.co.uk/news/live/world-middle-east-67527098",
    "https://www.bbc.co.uk/news/live/world-middle-east-67400490"
]

def scrape_bbc_live_article(url):
    """Scrape the live article content from a BBC live news page."""
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        items = soup.find_all('li')
        content = []
        for item in items:
            header = item.find('header')
            paragraph = item.find('p')
            if header and paragraph:
                header_text = header.get_text(strip=True)
                paragraph_text = paragraph.get_text(strip=True)
                content.append(f"{header_text}: {paragraph_text}")
        return '\n'.join(content)
    else:
        return f"Failed to fetch {url}: Status code {response.status_code}"

# Collect data for each live URL
live_articles_data = []
for url in live_urls:
    print(f"Scraping live URL: {url}")
    live_article_text = scrape_bbc_live_article(url)
    live_articles_data.append({"URL": url, "Content": live_article_text})

# Create a DataFrame and save it to an Excel file
df_live = pd.DataFrame(live_articles_data)
df_live.to_excel("bbc_live_articles.xlsx", index=False)

print("Live articles saved to bbc_live_articles.xlsx")
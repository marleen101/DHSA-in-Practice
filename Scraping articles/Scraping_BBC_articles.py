import requests
from bs4 import BeautifulSoup
import pandas as pd

# List of URLs to scrape
urls = [
    "https://www.bbc.co.uk/news/world-middle-east-67404110",
    "https://www.bbc.co.uk/news/world-middle-east-67306902",
    "https://www.bbc.co.uk/news/world-middle-east-67480680",
    "https://www.bbc.co.uk/news/world-middle-east-67332684",
    "https://www.bbc.co.uk/news/world-africa-67257862",
    "https://www.bbc.co.uk/news/world-middle-east-67535965",
    "https://www.bbc.co.uk/news/world-middle-east-67373293",
    "https://www.bbc.co.uk/news/world-middle-east-67493713",
    "https://www.bbc.co.uk/news/world-middle-east-67327079",
    "https://www.bbc.co.uk/news/world-middle-east-67361128",
    "https://www.bbc.co.uk/news/world-middle-east-67347201",
    "https://www.bbc.co.uk/news/world-middle-east-67084141",
    "https://www.bbc.co.uk/news/world-middle-east-67401064",
    "https://www.bbc.co.uk/news/world-67418110",
    "https://www.bbc.co.uk/news/world-middle-east-67518819",
    "https://www.bbc.co.uk/news/world-middle-east-67550483",
    "https://www.bbc.co.uk/news/world-middle-east-67302206",
    "https://www.bbc.co.uk/news/world-middle-east-67520263",
    "https://www.bbc.co.uk/news/world-middle-east-67575684",
    "https://www.bbc.co.uk/news/world-middle-east-67463162",
    "https://www.bbc.co.uk/news/world-middle-east-67320520",
    "https://www.bbc.co.uk/news/world-middle-east-67528844",
    "https://www.bbc.co.uk/news/world-middle-east-67554394",
    "https://www.bbc.co.uk/news/world-middle-east-67339008",
    "https://www.bbc.co.uk/news/world-asia-china-67237146",
    "https://www.bbc.co.uk/news/business-67497299",
    "https://www.bbc.co.uk/news/world-middle-east-67331176",
    "https://www.bbc.co.uk/news/world-middle-east-67530181",
    "https://www.bbc.co.uk/news/world-middle-east-67372035",
    "https://www.bbc.co.uk/news/world-middle-east-67372661",
    "https://www.bbc.co.uk/news/world-middle-east-67390375"
]

def scrape_bbc_article(url):
    """Scrape the article text from a BBC news page."""
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('div', {'data-component': 'text-block'})
        text_content = '\n'.join([p.get_text(strip=True) for p in paragraphs])
        return text_content
    else:
        return f"Failed to fetch {url}: Status code {response.status_code}"

# Collect data for each URL
articles_data = []
for url in urls:
    print(f"Scraping URL: {url}")
    article_text = scrape_bbc_article(url)
    articles_data.append({"URL": url, "Content": article_text})

# Create a DataFrame and save it to an Excel file
df = pd.DataFrame(articles_data)
df.to_excel("bbc_articles.xlsx", index=False)

print("Articles saved to bbc_articles.xlsx")
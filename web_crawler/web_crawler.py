import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
start_url = input("enter the url you want to scrape ")
visited = set()
to_visit = {start_url}
headers = {"User-Agent": "Mozilla/5.0"}
while to_visit:
    url = to_visit.pop()
    if url in visited:
        continue
    print(f"visiting {url}...")
    try:
        response = requests.get(url, headers=headers, timeout=10)
    except requests.RequestException:
        print(f"couldn't access {url} :( )")
    soup = BeautifulSoup(response.content, 'html.parser')
    for tag in soup.find_all("a"):
        link = tag.get("href")
        if link:
            full_url = urljoin(url, link)
            if urlparse(full_url).netloc == urlparse(start_url).netloc:
                to_visit.add(full_url)
    visited.add(url)

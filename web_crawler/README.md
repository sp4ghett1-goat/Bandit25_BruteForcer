# Web Crawler

A simple Python web crawler that starts from a given URL, discovers links on each page, and recursively visits other pages on the same website.

This project was built as a learning exercise to practice HTTP requests, HTML parsing, URL handling, and basic crawling logic.

## Features

* Start crawling from any URL
* Sends HTTP requests using `requests`
* Parses HTML using BeautifulSoup
* Finds links from `<a>` tags
* Converts relative URLs into full URLs
* Keeps track of visited pages
* Prevents crawling outside the starting website
* Handles inaccessible URLs with request exceptions
* Uses a custom User-Agent
* Uses a 10-second request timeout

## Requirements

* Python 3
* `requests`
* `beautifulsoup4`

Install the dependencies with:

```bash
pip install requests beautifulsoup4
```

## Usage

Run the crawler:

```bash
python3 web_crawler.py
```

Enter the URL you want to crawl:

```text
enter the url you want to scrape https://example.com
```

The crawler will then display the pages it visits:

```text
visiting https://example.com...
visiting https://example.com/about...
visiting https://example.com/contact...
```

## How It Works

### 1. Starting URL

The crawler asks the user for a starting URL.

```python
start_url = input("enter the url you want to scrape ")
```

The starting URL is placed into a set called `to_visit`.

### 2. Tracking URLs

Two sets are used:

* `to_visit` — URLs that still need to be crawled
* `visited` — URLs that have already been crawled

This prevents the crawler from repeatedly visiting the same pages.

### 3. Sending Requests

The crawler uses the `requests` library to retrieve each page.

A User-Agent is also included:

```python
headers = {"User-Agent": "Mozilla/5.0"}
```

The request has a 10-second timeout so the crawler does not wait indefinitely for a response.

### 4. Parsing HTML

BeautifulSoup parses the returned HTML:

```python
soup = BeautifulSoup(response.content, "html.parser")
```

The crawler then searches for `<a>` elements:

```python
soup.find_all("a")
```

These elements can contain links in their `href` attribute.

### 5. Handling URLs

Some links may be relative:

```text
/about
```

while others may already be complete:

```text
https://example.com/about
```

`urljoin()` converts them into complete URLs based on the current page.

`urlparse()` is then used to examine the domain.

### 6. Staying on the Same Website

The crawler compares the domain of each discovered URL with the domain of the original starting URL.

This means that if the crawler starts at:

```text
https://example.com
```

it can follow:

```text
https://example.com/about
https://example.com/contact
```

but will not automatically crawl:

```text
https://google.com
```

### 7. Crawling

Every discovered same-domain URL is added to `to_visit`.

The loop continues until there are no URLs left to visit.

## Python Concepts Practiced

* HTTP requests
* HTML parsing
* `requests`
* BeautifulSoup
* Sets
* `while` loops
* `try` / `except`
* Exception handling
* Functions from `urllib.parse`
* URL parsing
* Relative and absolute URLs
* User-Agent headers
* Recursion-like crawling through a queue/set

## Limitations

This is a beginner-level crawler and has several limitations:

* No crawl depth limit
* No rate limiting
* No robots.txt handling
* No concurrency
* Does not save discovered pages or links to a file
* Does not extract page content
* Does not distinguish different HTTP status codes
* Does not filter non-HTML resources such as PDFs or images
* Can potentially crawl a large number of pages on a website

## Future Improvements

Possible improvements include:

* Add a maximum crawl depth
* Add delays between requests
* Save discovered URLs to a file
* Display HTTP status codes
* Extract page titles
* Add command-line arguments
* Add concurrency for faster crawling
* Handle redirects
* Filter URLs by file type
* Implement robots.txt checking
* Add logging

## Disclaimer

Only crawl websites where you have permission to do so. Respect the website's terms, robots.txt rules, and server resources. Avoid sending excessive requests.

## What I Learned

This project helped me understand how a basic web crawler works internally instead of relying entirely on tools such as dedicated crawling frameworks.

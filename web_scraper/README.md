# Web Scraper

A simple Python web scraper that retrieves a webpage and uses BeautifulSoup to find HTML elements and their attributes.

This project was built as a learning exercise to practice HTTP requests, HTML parsing, functions, user input, and working with HTML elements.

## Features

* Scrape a webpage from a user-provided URL
* Search for HTML tags
* Find only the first matching tag
* Find all matching tags
* Extract a specific HTML attribute from matching tags
* Display the HTTP response status code
* Uses a custom User-Agent header
* Interactive command-line interface

## Requirements

* Python 3
* `requests`
* `beautifulsoup4`

Install the dependencies with:

```bash
pip install requests beautifulsoup4
```

## Usage

Run the scraper:

```bash
python3 web_scraper.py
```

The program will ask for a URL:

```text
what url would you like to scrape https://example.com
```

Then specify which HTML tag you want to search for:

```text
which tag would you like to find a
```

You can choose whether to find the first matching element or all matching elements:

```text
would you like to find everything containing that tag or just the first thing? first/all: all
```

Finally, the program asks whether you want to extract a specific attribute:

```text
would you like to find a certain attribute? y/n y
what is the attribute you want to find href
```

## Examples

### Find the first matching tag

If you search for:

```text
h1
```

and choose `first`, the scraper uses:

```python
soup.find(tag)
```

This returns the first matching `<h1>` element.

### Find all matching tags

Choosing `all` uses:

```python
soup.find_all(tag)
```

This returns every matching element on the page.

For example, searching for:

```text
a
```

can return all links on the page.

### Extract an attribute

You can also extract a specific attribute from every matching element.

For example, searching for the `href` attribute of `<a>` tags:

```python
t.get("href")
```

could produce:

```text
/about
/contact
https://example.com
```

## How It Works

### 1. Requesting the Page

The `requests` library downloads the webpage:

```python
response = requests.get(url, headers=headers)
```

A User-Agent is included to identify the request as coming from a browser-like client.

### 2. Parsing the HTML

BeautifulSoup parses the response:

```python
soup = BeautifulSoup(response.content, "html.parser")
```

This turns the HTML into a structure that Python can search through.

### 3. Finding Elements

The program supports two search modes:

* `find()` — returns the first matching element
* `find_all()` — returns all matching elements

### 4. Extracting Attributes

When attribute searching is enabled, the program loops through every matching element and retrieves the selected attribute.

For example:

```python
t.get("class")
```

or:

```python
t.get("href")
```

## Python Concepts Practiced

* HTTP requests
* HTML parsing
* BeautifulSoup
* Functions
* User input
* `while` loops
* `if` / `elif` / `else`
* `for` loops
* Dictionaries
* HTML tags and attributes
* Exception-free input validation
* Working with return values

## Limitations

This is a beginner-level scraper and currently has some limitations:

* No exception handling for failed HTTP requests
* Does not check whether the response contains HTML
* Does not handle redirects explicitly
* Does not save results to a file
* Does not support CSS selectors
* Does not extract page content beyond selected tags/attributes
* Requires manual interaction for every scrape
* Some websites may block automated requests

## Future Improvements

Possible improvements include:

* Add `try` / `except` for request errors
* Add request timeouts
* Add support for CSS selectors
* Save results to a file
* Add command-line arguments
* Extract text from elements
* Add support for multiple URLs
* Display cleaner output
* Add status-code/error handling

## Disclaimer

Only scrape websites where you have permission to do so. Respect website terms, robots.txt rules, and server resources.

## What I Learned

This project helped me understand how Python can retrieve webpages and turn raw HTML into searchable data using BeautifulSoup.

# Simple Web Fuzzer

A small Python web fuzzer built with `requests`.

The script takes a target URL and then tests a list of words or paths against it. Responses with a `404 Not Found` status are ignored, while other responses are displayed.

## Features

* Tests multiple URL paths automatically
* Reads wordlists from standard input
* Ignores `404` responses
* Displays the response data
* Displays the HTTP status code
* Displays the word that produced the response
* Uses Python's `requests` library

## Requirements

Python 3 and the `requests` library.

Install `requests` with:

```bash
pip install requests
```

## Usage

Run the fuzzer:

```bash
python3 fuzzer.py
```

Enter the target URL when prompted:

```text
what is the target ip? http://127.0.0.1
```

The script reads words from standard input, so you can provide a wordlist using a pipe or redirection:

```bash
cat wordlist.txt | python3 fuzzer.py
```

or:

```bash
python3 fuzzer.py < wordlist.txt
```

For example, if `wordlist.txt` contains:

```text
admin
login
api
robots.txt
```

the script will test:

```text
http://127.0.0.1/admin
http://127.0.0.1/login
http://127.0.0.1/api
http://127.0.0.1/robots.txt
```

## How It Works

The program loops through each line received from standard input:

```python
for word in sys.stdin:
```

It removes whitespace from each word:

```python
word = word.strip()
```

Then it sends a GET request to the target:

```python
res = requests.get(url=f"{url}/{word}")
```

If the server responds with `404`, the result is ignored:

```python
if res.status_code == 404:
    continue
```

For other responses, the script attempts to parse the response as JSON and prints the response data, HTTP status code, and tested word.

## What I Learned

* Using the `requests` library
* Making HTTP GET requests
* Working with HTTP status codes
* Reading data from standard input with `sys.stdin`
* Using pipes and input redirection in Linux
* Processing wordlists
* Building a basic web fuzzing tool
* Working with JSON responses

## Limitations

This is a simple learning project and is not intended to replace tools such as professional web fuzzers.

The script currently expects non-404 responses to contain valid JSON. If a server returns HTML or another format, `res.json()` may raise an error.

## Disclaimer

This project was created for educational purposes. Only use web fuzzing against systems you own or have explicit permission to test.

## Author

sp4ghett1

# Base64 Encoder & Decoder

A simple Python command-line tool that can encode text into Base64 and decode Base64 back into text.

The program lets the user choose between encoding and decoding, then asks for the input.

## Features

* Encode text using Base64
* Decode Base64-encoded text
* Case-insensitive encode/decode selection
* Simple command-line interface
* Uses Python's built-in `base64` module

## Usage

Run the program with:

```bash
python3 base64_encoder.py
```

Choose whether you want to encode or decode:

```text
do you want to encode or decode?? encode/decode: encode
```

The program will then ask for the text:

```text
what is the password you want to encode?
```

For decoding, provide a Base64-encoded string instead.

## How It Works

### Encoding

The program uses:

```python
base64.b64encode()
```

The input string is first converted into bytes using `.encode()`, then converted into Base64.

### Decoding

The program uses:

```python
base64.b64decode()
```

The Base64 data is decoded back into bytes and then converted into a string using `.decode()`.

## What I Learned

* Using Python's `base64` module
* Encoding and decoding data
* Converting strings to bytes
* Converting bytes back into strings
* Using functions
* Using conditional statements
* Taking and processing user input
* Using `.lower()` to handle different input capitalization

## Important Note

Base64 is **encoding, not encryption**.

It does not provide confidentiality or security. Anyone can decode Base64 data if they have the encoded value.

For example:

```text
hello
```

can be represented as:

```text
aGVsbG8=
```

This should not be used as a way to securely store passwords or sensitive information.

## Disclaimer

This project was created for educational purposes while learning Python and cybersecurity fundamentals.

## Author

sp4ghett1

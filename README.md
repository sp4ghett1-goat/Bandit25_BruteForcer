# Bandit 24 Brute-Forcer

A Python script created to solve the OverTheWire Bandit Level 24 challenge.

The challenge requires finding a four-digit PIN for a local TCP service. This script automatically tests every possible PIN from `0000` to `9999` until it receives a response indicating success.

## How It Works

1. Creates a TCP socket using Python's `socket` module.
2. Connects to `127.0.0.1` on port `30002`.
3. Prompts the user to enter the current Bandit password.
4. Generates every possible four-digit PIN.
5. Combines the password and PIN into the required format.
6. Sends the credentials to the service.
7. Checks the response from the server.
8. Stops when the correct PIN is found.

## Usage

Run the script with:

```bash
python3 bandit25_bruteforcer.py
```

The script will ask for the current Bandit password:

```text
Enter the Bandit password:
```

It then tests the PINs automatically.

The target service must be running on:

```text
127.0.0.1:30002
```

## What I Learned

* Creating TCP sockets with Python
* Using `socket.AF_INET`
* Using `socket.SOCK_STREAM`
* Connecting to a TCP service
* Sending and receiving data with sockets
* Formatting numbers with `:04d`
* Automating repetitive network requests
* Brute-forcing a limited PIN space
* Handling server responses in Python
* Taking user input instead of hardcoding credentials

## Example

The PIN is formatted as exactly four digits:

```python
f"{pin:04d}"
```

This means:

```text
0    → 0000
7    → 0007
42   → 0042
1234 → 1234
```

## Disclaimer

This script was created for the authorized OverTheWire Bandit CTF environment and is intended for educational purposes. Brute-force techniques should only be used against systems you own or have explicit permission to test.

## Author

sp4ghett1

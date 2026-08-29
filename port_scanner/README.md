# Port Scanner

A simple Python port scanner that checks a target IP for open TCP and responsive UDP ports.

This project was built as a networking and cybersecurity learning exercise to practice Python sockets and understand how basic port scanning works.

## Features

* Scan a custom IP address
* Choose a starting and ending port
* TCP scanning
* UDP scanning
* Scan both TCP and UDP
* Configurable socket timeout
* Reports open TCP ports
* Reports UDP ports that respond

## Requirements

* Python 3
* No external Python libraries are required

The scanner uses Python's built-in `socket` module.

## Usage

Run the program:

```bash
python3 port_scanner.py
```

You will be asked for:

1. The target IP address
2. The starting port
3. The ending port
4. Whether to scan TCP, UDP, or both

Example:

```text
what is the target ip?? 127.0.0.1
what is the starting port? 1
what is the ending port? 100
would you like to scan tcp/udp/both: tcp
```

Example output:

```text
+ port 22/tcp is open!
+ port 80/tcp is open!
```

## How It Works

### TCP

The scanner creates a TCP socket and attempts to connect to each port using `connect_ex()`.

A return value of `0` indicates that the connection succeeded, meaning the port is reachable and open.

### UDP

UDP does not establish a connection like TCP. Instead, the scanner sends a small packet to each port and waits for a response.

If a response is received, the port is reported as responsive.

A timeout does **not** necessarily mean that a UDP port is closed. UDP scanning is more difficult to determine accurately because many services do not respond to arbitrary packets.

## Python Concepts Practiced

* `socket`
* TCP sockets
* UDP sockets
* `connect_ex()`
* `sendto()`
* `recvfrom()`
* Socket timeouts
* `try` / `except`
* Loops
* User input
* Type conversion
* Conditional statements

## Limitations

This is a beginner-level scanner and is not intended to replace tools such as Nmap.

Some limitations include:

* TCP ports are scanned sequentially
* UDP results can be ambiguous
* No service/version detection
* No multithreading or asynchronous scanning
* No hostname resolution
* No advanced scan techniques

## Disclaimer

Only scan systems and networks that you own or have explicit permission to test.

## Future Improvements

Possible improvements include:

* Add multithreading for faster scans
* Add service/version detection
* Support hostnames
* Improve UDP detection
* Add command-line arguments
* Add colored output
* Add scan progress indicators
* Add a `--help` option
* Export scan results to a file

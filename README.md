# Darkint-Forum-Monitor
Monitoring tool for underground forums and onion services through Tor.

## Description

This project implements a monitoring tool designed to periodically check the availability of underground forums and onion services through the Tor network.

The script retrieves each target URL, measures its response time, extracts the page title and identifies common protection mechanisms such as CAPTCHAs and waiting queues.

## Features

* Monitoring of multiple forums and onion services.
* Tor support through a SOCKS5 proxy.
* HTTP status verification.
* Response time measurement.
* Automatic HTML title extraction.
* CAPTCHA detection.
* Waiting queue detection.
* Continuous monitoring with configurable intervals.

## Requirements

* Python 3
* requests
* beautifulsoup4
* PySocks

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the script:

```bash
python monitor.py
```

The tool will periodically check all configured URLs and display:

* HTTP status code
* Response time
* Page title
* Detected protections

Example output:

```text
OK | 200 | 2.1s | Exilio404
OK | 200 | 1.8s | DNA Forums
OK | 200 | 1.4s | dread Access Queue | COLA
OK | 200 | 6.5s | Verify Humanity | CAPTCHA
```

## Disclaimer

This software was developed for academic and research purposes only. Users are responsible for complying with all applicable laws and regulations.

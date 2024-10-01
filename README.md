A simple reconnaissance tool for ethical hacking and bug bounty hunting.

This tool is designed to perform various network reconnaissance tasks such as port scanning, DNS enumeration, and WHOIS lookup. It uses multithreading to speed up the process and handles common errors gracefully.

## Features
- Port scanning
- DNS enumeration
- WHOIS lookup

## Installation
1. Clone the repository
2. Create a virtual environment: `python3 -m venv YOUR-ENV-NAME`
3. Activate the virtual environment:
    - Windows: `YOUR-ENV-NAME\Scripts\activate`
    - macOS/Linux: `source YOUR-ENV-NAME/bin/activate`
4. Install the dependencies: `pip install -r requirements.txt`

## Usage

```bash
cd src
```

```bash
python3 -m recon-tool.main [target] --ports [port-range] --dns --whois
```

Example:
```bash
python3 -m recon-tool.main example.com --ports 1-1000 --dns --whois
```


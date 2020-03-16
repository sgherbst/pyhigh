import requests

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15'
}

def download(url, loc, timeout=5):
    r = requests.get(url, timeout=timeout, headers=HEADERS)
    with open(loc, 'wb') as f:
        f.write(r.content)
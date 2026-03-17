import requests

URLS = [
    "https://raw.githubusercontent.com/stamparm/ipsum/master/ipsum.txt",
    "https://urlhaus.abuse.ch/downloads/text/"
]

def fetch_url(url):
    try:
        response = requests.get(url, timeout=10)
        return response.text
    except:
        return ""

def get_all_sources():
    all_data = ""
    for url in URLS:
        print(f"[+] Coletando: {url}")
        all_data += fetch_url(url) + "\n"
    return all_data
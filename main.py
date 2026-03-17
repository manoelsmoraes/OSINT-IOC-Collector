import re
import requests

def get_data():
    url = "https://raw.githubusercontent.com/stamparm/ipsum/master/ipsum.txt"
    response = requests.get(url)
    return response.text

def extract_iocs(data):
    ips = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', data)
    domains = re.findall(r'\b[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b', data)
    return set(ips), set(domains)

def main():
    print("[+] Coletando dados OSINT...")
    data = get_data()

    print("[+] Extraindo IOCs...")
    ips, domains = extract_iocs(data)

    print(f"\n[+] Total de IPs encontrados: {len(ips)}")
    print(f"[+] Total de domínios encontrados: {len(domains)}")

    print("\n[+] Exemplos de IPs:")
    for ip in list(ips)[:10]:
        print(ip)

    print("\n[+] Exemplos de domínios:")
    for domain in list(domains)[:10]:
        print(domain)

if __name__ == "__main__":
    main()
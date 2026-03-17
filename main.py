import re
from sources import get_all_sources

def extract_iocs(data):
    ips = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', data)
    domains = re.findall(r'\b[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b', data)
    return set(ips), set(domains)

def save_results(ips, domains):
    with open("output/ips.txt", "w") as f:
        for ip in sorted(ips):
            f.write(ip + "\n")

    with open("output/domains.txt", "w") as f:
        for domain in sorted(domains):
            f.write(domain + "\n")

def main():
    print("=== OSINT IOC Collector v2 ===\n")

    print("[+] Coletando dados de múltiplas fontes OSINT...")
    data = get_all_sources()

    print("[+] Extraindo IOCs...")
    ips, domains = extract_iocs(data)

    print(f"[+] IPs únicos encontrados: {len(ips)}")
    print(f"[+] Domínios únicos encontrados: {len(domains)}")

    print("[+] Salvando resultados...")
    save_results(ips, domains)

    print("\n[+] Arquivos gerados em /output")
    print("✔️ Coleta finalizada com sucesso!")

if __name__ == "__main__":
    main()
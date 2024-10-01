import argparse
import json
from .port_scanner import PortScanner
from .dns_enum import DNSEnumerator
from .whois_lookup import WHOISLookup

def print_section(title):
    print(f"\n{'-' * 40}")
    print(f"{title:^40}")
    print(f"{'-' * 40}")

def print_dns_records(dns_records):
    for record_type, records in dns_records.items():
        print(f"    {record_type} Records:")
        if records:
            for record in records:
                print(f"        - {record}")
        else:
            print("        No records found")
        print()

def print_whois_info(whois_info):
    important_fields = [
        "domain_name",
        "registrar",
        "creation_date",
        "expiration_date",
        "name_servers",
        "status",
        "registrant_name",
        "registrant_organization",
        "registrant_country"
    ]

    for field in important_fields:
        if field in whois_info:
            value = whois_info[field]
            if isinstance(value, list):
                print(f"    {field.replace('_', ' ').title()}:")
                for item in value:
                    print(f"        - {item}")
            else:
                print(f"    {field.replace('_', ' ').title()}: {value}")
    print("\n   Other Details:")
    print(f"    {json.dumps(whois_info, indent=2, default=str)}")

def main():
    parser = argparse.ArgumentParser(description="Recon Tool")
    parser.add_argument("target", help="Target domain or IP address")
    parser.add_argument("--ports", help="Port range to scan (e.g., 1-1000)", default="1-1000")
    parser.add_argument("--dns", action="store_true", help="Perform DNS enumeration")
    parser.add_argument("--whois", action="store_true", help="Perform WHOIS lookup")

    args = parser.parse_args()

    print_section(f"Starting reconnaissance on {args.target}")

    if args.ports:
        print_section("Port Scanning")
        start_port, end_port = map(int, args.ports.split('-'))
        scanner = PortScanner(args.target)
        open_ports = scanner.scan(start_port, end_port)
        print(f"    Scanned ports: {start_port} - {end_port}")
        print(f"    Open ports: {', '.join(map(str, open_ports)) if open_ports else 'No open ports found'}")

    if args.dns:
        print_section("DNS Enumeration")
        dns_enum = DNSEnumerator(args.target)
        dns_records = dns_enum.enumerate()
        print_dns_records(dns_records)
        

    if args.whois:
        print_section("WHOIS Information")
        whois_lookup = WHOISLookup(args.target)
        whois_info = whois_lookup.lookup()
        print_whois_info(whois_info)

if __name__ == "__main__":
    main()
    
import dns.resolver
def dns_e(domain):
    try:
        print("\n=== DNS Enumeration Results ===")
        #A Record
        print("\n[+] A Record:")
        for a in dns.resolver.resolve(domain, 'A'):
            print(a.to_text())
        #MX Record
        print("\n[+] MX Record:")
        for mx in dns.resolver.resolve(domain, 'MX'):
            print(mx.to_text())
        #NS Record
        print("\n[+] NS Record:")
        for ns in dns.resolver.resolve(domain, 'NS'):
            print(ns.to_text())
    except dns.resolver.NoAnswer:
        print("\n[-] No DNS records found.")
    except dns.resolver.NXDOMAIN:
        print("\n[-] Domain does not exist.")
    except Exception as e:
       print(f"\n[!] Error: {e}")

domain = input("Enter domain name: ")
dns_e(domain)

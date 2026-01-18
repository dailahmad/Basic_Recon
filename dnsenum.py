import dns.resolver
def dnsenum(domain):
    print("\nDNS Enumeration Results")
    try:
        #A
        print("\n[+] A Record:")
        for rdata in dns.resolver.resolve(domain, 'A'):
            print(rdata.to_text())
    except:
        print("Not found")
    try:
        #AAAA
        print("\n[+] AAAA Record:")
        for rdata in dns.resolver.resolve(domain, 'AAAA'):
            print(rdata.to_text())
    except:
        print("Not found")
    try:
        #MX
        print("\n[+] MX Record:")
        for rdata in dns.resolver.resolve(domain, 'MX'):
            print(rdata.to_text())
    except:
        print("Not found")
    try:
        #NS
        print("\n[+] NS Record:")
        for rdata in dns.resolver.resolve(domain, 'NS'):
            print(rdata.to_text())
    except:
        print("Not found")
    try:
        #TXT
        print("\n[+] TXT Record:")
        for rdata in dns.resolver.resolve(domain, 'TXT'):
            print(rdata.to_text())
    except:
        print("Not found")

domain = input("Enter domain name: ")
dnsenum(domain)

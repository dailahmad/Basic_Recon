import whois
def whoislookup(domain):
    try:
        w = whois.whois(domain)
        print("\nWHOIS Lookup Results")
        print(f"\nRegistrar      : {w.registrar}")
        print(f"Creation Date  : {w.creation_date}")
        print(f"Expiry Date    : {w.expiration_date}")
        print("\nName Servers:")
        if w.name_servers:
            for ns in w.name_servers:
                print(ns)
        else:
            print("Not available")
    except Exception as e:
        print(f"\n[!] Error performing WHOIS lookup: {e}")

domain = input("Enter domain name: ")
whoislookup(domain)

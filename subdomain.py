import requests
import json
def subdomain_enum(domain):
    print("\nSubdomain Enumeration Results")
    url = f"https://crt.sh/?q={domain}&output=json"
    try:
        response = requests.get(url, timeout=10)
        data = json.loads(response.text)
        subdomains = set()
        for entry in data:
            name_value = entry.get("name_value", "")
            names = name_value.split("\n")
            for name in names:
                #Remove wildcard
                if name.startswith("*."):
                    name = name[2:]
                #Only subdomains of target domain
                if name.endswith(domain):
                    subdomains.add(name.strip())
        #results
        sorted_subdomains = sorted(subdomains)
        if sorted_subdomains:
            for sub in sorted_subdomains:
                print(sub)
        else:
            print("No subdomains found.")
    except Exception as e:
        print(f"[!] Error: {e}")

domain = input("Enter domain name: ")
subdomain_enum(domain)

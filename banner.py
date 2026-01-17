import socket
def grab_banner(ip, port):
    try:
        #TCP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        #Connection
        s.connect((ip, port))
        #request
        s.send(b"Hello\r\n")
        # Receive
        banner = s.recv(1024)
        if banner:
            print("\n[+] Banner received:")
            print(banner.decode(errors="ignore"))
        else:
            print("\n[-] No banner received.")
        s.close()
    except socket.timeout:
        print("\n[!] Connection timed out.")
    except ConnectionRefusedError:
        print("\n[!] Connection refused.")
    except Exception as e:
        print(f"\n[!] Error: {e}")

ip = input("Enter target IP: ")
port = int(input("Enter target port: "))

grab_banner(ip, port)

import csv
import socket
import datetime

def internet(host="8.8.8.8", port=53, timeout=5):
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        print(ex)
        return False

connected = internet()
with open('connections.csv','a') as f:
    writer = csv.writer(f)
    writer.writerow([datetime.datetime.now(), connected])
import socket
scan_host = input("Enter a host : ")
scan_ip  = socket.gethostbyname(scan_host)
for port in range(1,65535):  
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    results = sock.connect_ex((scan_ip, port))
    if results == 0:
        print("Port {}: 	 Open".format(port))
    sock.close()
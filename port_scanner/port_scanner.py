import socket
target_ip = input("what is the target ip?? ")
start_port = int(input("what is the starting port? "))
end_port = int(input("what is the ending port? "))
while True:
    choice = input("would you like to scan tcp/udp/both: ").lower()
    if choice == "tcp" or choice == "udp" or choice == "both":
        break
    else:
        print("invalid option it's either tcp or udp or both :) ") 
if choice == "tcp":
    for port in range(start_port, end_port + 1):
        tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_sock.settimeout(0.5)
        tcp_resault = tcp_sock.connect_ex((target_ip, port))
        if tcp_resault == 0:
            print(f"+ port {port}/tcp is open!")
        tcp_sock.close()
elif choice == "udp":
    for port in range(start_port, end_port + 1):
            udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            udp_sock.settimeout(0.5)
            udp_sock.sendto(b"hello", (target_ip, port))
            try:
                data, adress = udp_sock.recvfrom(1024)
                print(f"+ {port}/udp responded!")
            except socket.timeout:
                 print(f"? port {port}/udp no response")
            udp_sock.close()
elif choice == "both":
    for port in range(start_port, end_port + 1):
            tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp_sock.settimeout(0.5)
            tcp_resault = tcp_sock.connect_ex((target_ip, port))
            if tcp_resault == 0:
                print(f"+ port {port}/tcp is open!")
            tcp_sock.close()
    for port in range(start_port, end_port + 1):
            udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            udp_sock.settimeout(0.5)
            udp_sock.sendto(b"hello", (target_ip, port))
            try:
                data, adress = udp_sock.recvfrom(1024)
                print(f"+ {port}/udp responded!")
            except socket.timeout:
                 print(f"? port {port}/udp no response")
            udp_sock.close()
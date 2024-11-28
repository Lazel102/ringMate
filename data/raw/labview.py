import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(("0.0.0.0", 8004))

print("Listening for UDP packets on localhost...")

while True:
    data, address = udp_socket.recvfrom(1024)
    print(f"Received message: {data.decode()} from {address}")
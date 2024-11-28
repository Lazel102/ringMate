import socket
import struct

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(("0.0.0.0", 8004))

print("Listening for UDP packets on localhost...")

while True:
    data, address = udp_socket.recvfrom(1024)  # Receive up to 1024 bytes
    print(f"Received raw data: {data} from {address}")

    try:
        # Attempt to decode if it's valid UTF-8
        integer_part = struct.unpack('!I', data[:4])[0]  # First 4 bytes as an integer
        floats_part = struct.unpack('!fff', data[4:])  # Next 12 bytes as 3 floats

        print(f"Integer: {integer_part}")
        print(f"Floats: {floats_part}")

    except:
        print("Data is not valid UTF-8; received raw bytes.")
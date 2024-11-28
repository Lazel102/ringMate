import socket
import struct
import socket
import struct
import json
import time
import os
from os.path import curdir


def listen_to_labview():
    udp_socket.bind(("0.0.0.0", 8004))
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

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




def record_udp_data(output_file, duration=10):
    """
    Records UDP data for a specified duration and saves it to a JSON file.

    Parameters:
        output_file (str): Path to save the JSON file.
        duration (int): Time in seconds to record data.
    """
    current_dir = os.getcwd()

    # Define the directory and file path

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("0.0.0.0", 8004))

    print(f"Listening for UDP packets on port 8004 for {duration} seconds...")
    start_time = time.time()
    recorded_data = []

    while time.time() - start_time < duration:
        try:
            data, address = udp_socket.recvfrom(1024)  # Receive up to 1024 bytes
            integer_part = struct.unpack('!I', data[:4])[0]  # First 4 bytes as an integer
            floats_part = struct.unpack('!fff', data[4:])  # Next 12 bytes as 3 floats

            entry = {
                "integer": integer_part,
                "coordinates": {"x": floats_part[0], "y": floats_part[1], "z": floats_part[2]},
                "timestamp": time.time(),
                "source": address[0]
            }
            recorded_data.append(entry)

            print(f"Recorded data: {entry}")
        except Exception as e:
            print(f"Error processing data: {e}")

    udp_socket.close()

    # Save recorded data to JSON
    with open(output_file, "w") as file:
        json.dump(recorded_data, file, indent=4)

    print(f"Data recording complete. Saved to {output_file}")

current_dir = os.getcwd()
output_dir = os.path.join(current_dir, 'json/we2.json')
# Example usage
record_udp_data(output_dir, duration=10)

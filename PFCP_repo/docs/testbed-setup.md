# Testbed Setup

## Hardware

| Item | Specification |
|---|---|
| Host platform | Standalone computing platform |
| CPU | AMD Ryzen 5 7530U @ 2.0 GHz |
| RAM | 16 GB |
| Host OS | Ubuntu 22.04 |

## Virtualized topology

The experimental 5G Core is logically separated across Ubuntu-based virtual machines:

- AMF — dedicated VM
- SMF — dedicated VM
- UPF — dedicated VM(s)
- UERANSIM — gNB/UE emulation VM
- NWDAF — integrated with the Open5GS core VM

The N4 path between SMF and UPF is the primary observation point for PFCP analytics.

## Software

| Component | Version |
|---|---|
| Open5GS | 2.7.1 |
| UERANSIM | Specify exact experimental version |
| Python | Specify exact version |
| Scapy | Specify exact version |

## Reproduction order

1. Deploy the isolated Open5GS/UERANSIM testbed.
2. Establish legitimate PDU sessions.
3. Capture PFCP traffic on the authorized N4 observation point.
4. Execute one attack scenario at a time.
5. Preserve the corresponding PCAP and detector output.
6. Compare attack traffic with the benign baseline.
7. Evaluate alert timing and detection accuracy.

Exact network addresses, PLMN values, credentials, and deployment-specific settings should be added to private configuration files rather than hard-coded into the public repository.

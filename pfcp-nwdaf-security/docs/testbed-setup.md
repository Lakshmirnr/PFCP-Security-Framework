# Testbed Setup

## Hardware
| Item | Spec |
|---|---|
| Host platform | Standalone computing platform |
| CPU | AMD Ryzen 5 7530U @ 2.0 GHz |
| RAM | 16 GB |
| OS (host) | Ubuntu 22.04 |

## Virtualization / Topology
Multiple Ubuntu-based VMs were provisioned on the host, each assigned a dedicated network function to preserve logical separation between components:

- **AMF** — dedicated VM
- **SMF** — dedicated VM
- **UPF** — dedicated VM(s); additional UPF instances provisioned on separate VMs for user-plane scalability testing
- **UERANSIM** (gNB + UE emulation) — dedicated VM
- **NWDAF** — integrated within the Open5GS core VM (shares resources; no dedicated CPU/memory quota)

Dedicated virtual network interfaces and bridges were configured to separate control-plane and user-plane traffic and to enable UE-to-core connectivity.

## Software Versions
| Component | Version |
|---|---|
| Open5GS | 2.7.1 |
| UERANSIM | TODO |
| Python | TODO |
| Scapy | TODO |

## Open5GS Configuration Notes
[TODO: document any non-default configuration — e.g., number of UPF instances, PLMN/TAC values, slice configuration, DNN settings — that a reader would need to reproduce your results.]

## Reproducing the Attacks
See each folder under [`../attacks/`](../attacks/) for step-by-step instructions specific to each of the four vulnerabilities discussed in the paper.

## Reproducing the Detection Mechanism
See [`../nwdaf-detection/`](../nwdaf-detection/).

# Attack 1: [TODO: Attack Name, e.g., PFCP Session Establishment Spoofing]

## Description
[TODO: 2-3 sentences describing the vulnerability being exploited, which PFCP message type(s) are involved, and the attacker's assumed position (e.g., inline on N4, spoofed SMF/UPF).]

## Related Paper Section
Section [TODO] — Figure [TODO]

## Prerequisites
- Open5GS v2.7.1 core running with SMF/UPF reachable on N4
- Python 3.x with Scapy installed (`pip install -r ../../requirements.txt`)
- Attacker host with network access to the N4 interface segment

## How to Run
```bash
python3 attack.py --target <SMF/UPF IP> --iface <interface name>
```

## Parameters
| Parameter | Description | Default |
|---|---|---|
| `--target` | Target SMF/UPF IP address | - |
| `--iface` | Network interface to send crafted packets | - |
| TODO | TODO | TODO |

## Expected Behavior / Impact
[TODO: What should the operator/defender observe if the attack succeeds — e.g., session table corruption, resource exhaustion, unauthorized session modification.]

## Detection
This attack is detected by the custom NWDAF module in [`../../nwdaf-detection`](../../nwdaf-detection), via the `[TODO: Analytics ID name]` analytics output.
